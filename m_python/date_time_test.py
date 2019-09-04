from datetime import date
from datetime import time
from datetime import datetime


def test_date_today():
    today = date.today()

    print(today.month)
    print(today.day)
    print(today.weekday())
    assert today.year >= 2018
