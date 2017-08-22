import datetime
import os

BASE_DIR = os.path.dirname(__file__)


def _get_date():
    datetemp = []
    with open(get_projectfile('date.res'), 'r', encoding='utf-8') as f:
        for line in f.readlines():
            datetemp.append(line.strip())
    return datetemp


def _set_date(new_date):
    with open('date.res', mode='w+', encoding='utf-8') as f:
        f.write(new_date)
        f.flush()


def get_projectfile(filename):
    return os.path.join(BASE_DIR, filename)


def _add_date(date):
    dt = datetime.datetime.strptime(date[0], "%Y%m%d")
    d = dt + datetime.timedelta(hours=24)
    new_date = d.strftime('%Y%m%d')
    return new_date

with open('date.res', mode='w+', encoding='utf-8') as f:
    f.write(newd)
    f.flush()
