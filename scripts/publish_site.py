"""Report deployment triggered by a main-branch push; optionally redeploy manually."""
import argparse
import subprocess

from build_site import ROOT, SITE_URL

REPOSITORY = 'OWD-AI/awesome-open-world-discovery'


def publish(redeploy=False):
    # Compatibility entry point for the local monitor; no separate repository.
    if redeploy:
        subprocess.run(['gh', 'workflow', 'run', 'pages.yml', '--repo', REPOSITORY, '--ref', 'main'], cwd=ROOT, check=True)
        print('Requested a fresh Pages deployment:', SITE_URL)
    else:
        print('The main-branch push triggers the Pages workflow:', SITE_URL)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--redeploy', action='store_true')
    args = parser.parse_args()
    publish(args.redeploy)
