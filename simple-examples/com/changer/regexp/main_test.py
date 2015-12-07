#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

print("==========01==================")
src = "hello world";
p1 = re.compile(r"hello")
m1 = p1.match(src)
print(m1)
print(m1.group(0))


print("=========02===================")
src = "world hello"
p2 = re.compile(r"hello")
m2 = p2.match(src)
if m2:
    print("有匹配的", m2)
else:
    print("没有匹配的")
m2 = p2.search(src)
if m2:
    print("用search匹配,有匹配的", m2)
else:
    print("用search匹配,没有匹配的")

print("=========03===================")
src = "hello hella helol helloooo"
result = re.sub(r"hell", "hihi", src)
print(result)

result = re.subn(r"hell", "hihi", src)
print(result)

print("=========04===================")
src = "123+456*789-765"
result = re.split(r"[\+\-\*]", src)
print(result)
