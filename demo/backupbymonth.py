#!/usr/bin/python3
# -*- coding: utf-8 -*-

import http.client
import time


def backupbymonth():
    try:
        url = []
        url.append("192.168.0.126")
        url.append(8070)
        data = "month" + time.strftime('%Y%m%d', time.localtime(
            time.time() - 24 * 60 * 60)) + "days=1"
        url.append("schedule/backup/month/" + data)
        client = http.client.HTTPConnection(url[0], url[1], timeout=30)
        client.request('GET', "/" + url[2])
        response = client.getresponse()
        print(response.status)
    except Exception as e:
        print('except:', repr(e))
    finally:
        if client:
            client.close()

backupbymonth()