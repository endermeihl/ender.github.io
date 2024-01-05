#!/usr/bin/python3
# -*- coding: utf-8 -*-

import http.client
import time


def backupeverday():
    try:
        url = []
        url.append("192.168.0.126")
        url.append(8070)
        data = "targets=exam,train,vrexam&startday=" + time.strftime('%Y%m%d', time.localtime(
            time.time() - 24 * 60 * 60 *100)) + "&days=1"
        url.append("schedule/backup?" + data)
        client = http.client.HTTPConnection(url[0], url[1], timeout=30)
        client.request('GET', "/" + url[2])
        response = client.getresponse()
        print(response.status)
        client.close()
    except Exception as e:
        print('except:', repr(e))

backupeverday()
