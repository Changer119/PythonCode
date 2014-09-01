#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
req = urllib2.Request("http://www.baiud.com")
response = urllib2.urlopen(req)
htmlText = response.read()
print htmlText

