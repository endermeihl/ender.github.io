#!/usr/bin/python3
# -*- coding: utf-8 -*-

import http.client
import datetime
import os

BASE_DIR = os.path.dirname(__file__)


def get_projectfile(filename):
    return os.path.join(BASE_DIR, filename)


def _set_date(new_date):
    with open('date.res', mode='w+', encoding='utf-8') as f:
        f.write(new_date)
        f.flush()


def _get_date():
    datetemp = []
    with open(get_projectfile('date.res'), 'r', encoding='utf-8') as f:
        for line in f.readlines():
            datetemp.append(line.strip())
    return datetemp


def _add_date(date):
    dt = datetime.datetime.strptime(date, "%Y%m%d")
    d = dt + datetime.timedelta(hours=24)
    new_date = d.strftime('%Y%m%d')
    return new_date


def backupold():
    try:
        url = []
        date = _get_date()[0]
        print(date)
        url.append("api.junruizx.com")
        url.append(80)
        data = "targets=exam,train,vrexam&startday=" + date + "&days=1"
        url.append("schedule/backup?" + data)
        client = http.client.HTTPConnection(url[0], url[1], timeout=30)
        client.request('GET', "/" + url[2])
        response = client.getresponse()
        _set_date(_add_date(date))
        print(response.status)
    except Exception as e:
        print('except:', repr(e))
    finally:
        if client:
            client.close()


backupold()
