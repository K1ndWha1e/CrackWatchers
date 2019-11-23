import datetime
import re


def cracked_date_after(cracked_day, release_day):
    try:
        return calculate_date(cracked_day, release_day)
    except AttributeError:
        return '0 day'


def calculate_date(cracked_day, release_day):
    release_date = datetime.datetime.strptime(release_day.replace('-', ''), "%Y%m%d").date()
    cracked_date = datetime.datetime.strptime(cracked_day.replace('-', ''), "%Y%m%d").date()
    ppp = cracked_date - release_date
    cracked_after = re.match(r'-{0,1}\d{1,4}\s{1}\w{3,4}', str(ppp)).group()

    return cracked_after


