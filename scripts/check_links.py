"""Bounded URL reachability check. Does not claim scientific or semantic validity."""
import argparse
import concurrent.futures
import html
import json
import re
import threading
import time
import urllib.error
import urllib.request
from urllib.parse import urlsplit
from build import ROOT,RELATED,load

parser=argparse.ArgumentParser()
parser.add_argument('--workers',type=int,default=4)
parser.add_argument('--timeout',type=float,default=12)
parser.add_argument('--output',default='.local/link-check.json')
args=parser.parse_args()
data,bench=load()
urls=sorted({x['url'] for r in data['resources'] for x in r['links']} | {p['evidence'] for p in bench['profiles']} | {x[1] for x in RELATED})
urls=sorted(set(urls) | {r['publication']['source_url'] for r in data['resources'] if r['kind']=='paper'})
lock=threading.Lock()
next_host={}

def check(url):
    host=urlsplit(url).hostname
    # Bound repeated requests to a primary-source host rather than stampeding it.
    with lock:
        slot=max(time.monotonic(),next_host.get(host,0))
        next_host[host]=slot+.8
    delay=slot-time.monotonic()
    if delay>0:
        time.sleep(delay)
    record={'url':url}
    request=urllib.request.Request(url,headers={'User-Agent':'AwesomeOpenWorldDiscovery-LinkCheck/1.0','Range':'bytes=0-65535'})
    try:
        with urllib.request.urlopen(request,timeout=args.timeout) as response:
            body=response.read(65536)
            record.update(status=response.status,result='reachable',resolved_url=response.url)
            if 'html' in response.headers.get('Content-Type',''):
                title=re.search(r'<title[^>]*>(.*?)</title>',body.decode('utf-8',errors='replace'),re.I|re.S)
                if title:
                    record['page_title']=html.unescape(re.sub(r'\s+',' ',title[1])).strip()
    except urllib.error.HTTPError as exc:
        record.update(status=exc.code,result='restricted-or-rate-limited' if exc.code in {401,403,418,429} else 'http-error',resolved_url=exc.url)
    except Exception as exc:
        record.update(status=None,result='network-error',error=type(exc).__name__+': '+str(exc)[:180])
    return record

with concurrent.futures.ThreadPoolExecutor(max_workers=max(1,min(args.workers,8))) as pool:
    results=list(pool.map(check,urls))
counts={key:sum(x['result']==key for x in results) for key in sorted({x['result'] for x in results})}
report={'snapshot_date':data['updated'],'scope':'HTTP reachability only; not a content audit, method verification or independent reproduction','counts':counts,'links':results}
out=(ROOT/args.output).resolve()
if not out.is_relative_to(ROOT):
    raise ValueError('Output must stay inside the repository')
out.parent.mkdir(parents=True,exist_ok=True)
with out.open('w',encoding='utf-8',newline='\n') as f:
    json.dump(report,f,ensure_ascii=False,indent=2)
    f.write('\n')
print(json.dumps({'checked':len(results),'counts':counts,'report':str(out.relative_to(ROOT))}))
for r in results:
    if r['result']!='reachable':
        print(json.dumps(r,ensure_ascii=True))
