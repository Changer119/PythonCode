# !/usr/bin/python
# -*- coding: <utf-8> -*-

import sys
print(sys.version)

a = "A2C"
print(a)
a_bytes = a.encode("utf-8")
print(a_bytes)

print(sys.getdefaultencoding())
b = u"蓝翔挖掘机"
print(b)
# b_bytes = b.encode("utf-8")
# print(b_bytes)