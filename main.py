
import webbrowser
import requests
import argparse
import time
import sys


DEFAULT_TIME_WAIT = 0.2
HEB_MAIN_URL = 'https://vaccine.heb.com/scheduler'
HEB_SCHEDULER_URL = (
    'https://heb-ecom-covid-vaccine.hebdigital-prd.com/vaccine_locations.json'
)


def print_std_out(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()


def handle_args():
    description = 'Attempt to schedule HEB Vaccine appointment'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        '-l',
        '--locations',
        nargs='+',
        required=True,
        help='List of locations that you are willing to go to'
    )
    args = parser.parse_args()
    return args


def main():
    args = handle_args()
    location_list = []
    for loc in args.locations:
        location_list.append(loc.lower().strip())

    browser = webbrowser.get(
        "C:/Program Files/Mozilla Firefox/firefox.exe %s"
    )
    browser.open(HEB_MAIN_URL)
    while True:
        try:
            results = requests.get(HEB_SCHEDULER_URL)
            results.raise_for_status()
        except Exception:
            print_std_out('\nError ocurred so wait then resume')
            time.sleep(2)
            continue

        data = results.json()
        found = False
        # Grab the first one it comes to and break out
        for location in data.get('locations'):
            if (
                location.get('city').lower() in location_list and
                location.get('url')
            ):
                browser.open_new_tab(location.get('url'))
                input('\nHit enter to continue running')
                break

        print_std_out('.')
        time.sleep(DEFAULT_TIME_WAIT)


if __name__ == '__main__':
    main()
