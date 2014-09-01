#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import Request, URLError, HTTPError, urlopen

old_url = "http://rrurl.cn/b1UZuP"
req = Request(old_url)
resp = urlopen(req)
# print "old url is " + old_url
# print "real url is " + resp.geturl()
print "info()"
print resp.info()