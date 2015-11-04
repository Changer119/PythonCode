# !/usr/bin/python
# -*- coding: <utf-8> -*-

import re

str = "<ebank><name>fcjiang</name><gender>male</gender><addr><province>hunan</province><city>hengyang</city></addr></ebank>"
matchObj = re.match(r'<name>(.*)</name>', str, 0)
print(matchObj.group())

