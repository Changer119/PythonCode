#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost", 20000))
print("Sending START")
for i in range(10):
    content = "hello--" + str(i)
    print(content)
    s.send(content.encode(encoding="utf-8"))
print("Sending END")

