"""check.py: python check.py --help for usage"""

__author__ = "Srikanth Mujjiga"
__copyright__ = "Check LICENSE file"
___email__ = "smujjiga[at]outlook.com"

import argparse
import time
from datetime import datetime, timedelta

import requests


class Session:
    def __init__(self, session_info):
        # session_id, date, available_capacity, min_age_limit, vaccine, slots:
        for key in session_info:
            setattr(self, key, session_info[key])

    def __str__(self):
        rep = "Data: {0}, capacity: {1}, Age Limit: {2}, Slots: {3}".format(
            self.date, self.available_capacity, self.min_age_limit, self.slots
        )
        return rep


class Center:
    def __init__(self, center_info):
        # center_id, name, state_name, district_name, block_name, pincode, lat, long, time_from, time_to, free_type, sessions
        for key in center_info:
            if key == "sessions":
                sessions_info = center_info[key]
                self.sessions = [
                    Session(sessions_info[i]) for i in range(len(sessions_info))
                ]
            else:
                setattr(self, key, center_info[key])

    def __str__(self):
        self.print(-1)

    def print(self, onlythis=-1):
        rep = ""
        for attr in dir(self):
            if attr == "print":
                continue

            if not attr.startswith("__") and attr != "sessions":
                rep += f"{attr:15}:  {getattr(self, attr)} \n"

        sessions = self.sessions
        rep += "Sessions:\n"
        for i, session in enumerate(sessions):
            if onlythis == -1 or onlythis == i:
                rep += f"{session.__str__()}\n"
        return rep


def check(district_id, date, age_limit=18, exact_date=False):
    count = 0
    # date : day-month-year Example "06-05-2021"
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
    params = {"district_id": district_id, "date": date}

    url = requests.get(url=url, params=params)
    response = url.json()

    all_centers = []
    for center in response["centers"]:
        all_centers.append(Center(center))

    for center in all_centers:
        for i, session in enumerate(center.sessions):
            if session.min_age_limit <= age_limit:
                if not exact_date or session.date == date:
                    count += 1
                    print(center.print(i))
    return count


def main(args):
    delay_min_sec = args.every_n_minutes * 60

    while True:
        print(f"*** Checking at {datetime.now()} ***\n")
        count = check(args.district_id, args.date, args.min_age_limit, args.exact_date)
        if count > 0:
            print(f"*** Found {count} possibilities ***")
        else:
            print("*** Found None ***")

        next_at = datetime.now() + timedelta(minutes=args.every_n_minutes)
        print(f"*** Will check again at {next_at} ***")
        time.sleep(delay_min_sec)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check the free slots",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    now = datetime.now()
    date = f"{now.day}-{now.month}-{now.year}"
    parser.add_argument(
        "--district_id",
        type=int,
        help="Default: 294, (which is Bangalore, BBMP)",
        default=294,
    )
    parser.add_argument("--date", type=str, help="Default: Today", default=date)
    parser.add_argument(
        "--min_age_limit", type=int, help="Default: 18 (use 45 or 18)", default=45
    )
    parser.add_argument("--every_n_minutes", type=int, help="Default: 60", default=60)
    parser.add_argument(
        "--exact_date", action="store_true", help="Check exact date", default=False
    )

    args = parser.parse_args()
    main(args)
