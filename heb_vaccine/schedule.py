
import webbrowser
import requests
import argparse
import platform
import time
import sys


DEFAULT_TIME_WAIT = 0.2
HEB_MAIN_URL = 'https://vaccine.heb.com/scheduler'
HEB_SCHEDULER_URL = (
    'https://heb-ecom-covid-vaccine.hebdigital-prd.com/vaccine_locations.json'
)


def print_std_out(msg) -> None:
    # Helper to just write out to screen immediately
    sys.stdout.write(msg)
    sys.stdout.flush()


def handle_args() -> argparse.Namespace:
    description = 'Attempt to schedule HEB Vaccine appointment'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        '-b',
        '--browser-path',
        default='C:/Program Files/Mozilla Firefox/firefox.exe',
        help='Windows path to your browser if on windows'
    )
    parser.add_argument(
        '-l',
        '--locations',
        nargs='+',
        required=True,
        help='List of locations that you are willing to go to'
    )

    args = parser.parse_args()
    return args


def main() -> None:
    args = handle_args()
    location_list = []
    for loc in args.locations:
        location_list.append(loc.lower().strip())

    if platform.system() != 'Windows':
        # On mac we can get away with just calling firefox
        browser = webbrowser.get('firefox')
    else:
        # Set the path of the browser for windows
        browser = webbrowser.get(f"{args.browser_path} %s")

    # Open the main HEB vaccine site list
    browser.open(HEB_MAIN_URL)
    while True:
        try:
            results = requests.get(HEB_SCHEDULER_URL)
            results.raise_for_status()
        except Exception:
            print_std_out(
                '\nError/timeout has ocurred. Waiting and will resume.\n'
            )
            time.sleep(2)
            continue

        data = results.json()
        # Grab the first one it comes to and break out
        for location in data.get('locations'):
            if (
                location.get('city').lower() in location_list and
                location.get('url')
            ):
                # Open the URL in the data to show the form
                browser.open_new_tab(location.get('url'))
                # Wait for a key press to continue running
                input('\nHit enter to continue running')
                break

        print_std_out('.')
        time.sleep(DEFAULT_TIME_WAIT)


if __name__ == '__main__':
    main()
