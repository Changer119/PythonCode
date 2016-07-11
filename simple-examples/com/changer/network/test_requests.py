#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

url = 'http://httpbin.org/post'

params = {
    "name": "fcjiang",
    "age": 12
}
headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}

resp = requests.post(url, data=params, headers=headers);
print(resp.text)
print("=========================")
print(resp.content)
print("=========================")
print(resp.json())