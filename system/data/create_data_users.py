import os
import sys
import csv
import random
import string
import datetime
from django.contrib.auth.hashers import make_password

# dir constants
DIR_CURR = os.path.dirname(os.path.abspath(__file__))
DIR_BASE = os.path.dirname(DIR_CURR)
DIR_DJANGO = os.path.join(DIR_BASE, "django", "kisho")

# django password
sys.path.append(DIR_DJANGO)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kisho.settings")

# number of users
NUM_USERS = 10000

# random strings
LEN_USERNAME = 8
LEN_PASSWORD = 16
FILE_OUTPUT = os.path.join(DIR_CURR, "users.csv")
CHOICE_USERNAME = string.ascii_letters
CHOICE_PASSWORD = string.ascii_letters + string.digits

# check uniqueness
USERNAMES = set()
PASSWORDS = set()

# date
START_DATE = datetime.date(2000, 1, 1)
END_DATE = datetime.datetime.today().date()
TIME_BETWEEN_DATES = END_DATE - START_DATE
DAYS_BETWEEN_DATES = TIME_BETWEEN_DATES.days

# csv header
CSV_HEADER = [
    "id", "username", "password", "date_joined", "is_active", "is_staff",
    "is_superuser", "raw_password"
]
CSV_ADMIN_USER = [
    1, "admin",
    make_password("admin"), "2000-01-01", 1, 1, 1, "admin"
]


def get_random_date():
    rand_days = random.randrange(DAYS_BETWEEN_DATES)
    rand_date = START_DATE + datetime.timedelta(days=rand_days)
    return str(rand_date)


def get_random_string(length, choices, checkset=set()):
    rand_str = "".join(random.choice(choices) for i in range(length))
    while rand_str in checkset:
        rand_str = "".join(random.choice(choices) for i in range(length))
    return rand_str


def get_random_username():
    return get_random_string(LEN_USERNAME, CHOICE_USERNAME, USERNAMES)


def get_random_password():
    return get_random_string(LEN_PASSWORD, CHOICE_PASSWORD, PASSWORDS)


def main():
    with open(FILE_OUTPUT, "w", newline="") as result:
        writer = csv.writer(result)
        writer.writerow(CSV_HEADER)
        writer.writerow(CSV_ADMIN_USER)
        for i in range(NUM_USERS):
            username = get_random_username()
            password = get_random_password()
            date_joined = get_random_date()
            row = [
                i + 2, username,
                make_password(password), date_joined, 1, 0, 0, password
            ]
            writer.writerow(row)
            print("\r{0}".format(i), end="")


if __name__ == "__main__":
    main()