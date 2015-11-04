# !/usr/bin/python
# -*- coding: <utf-8> -*-

with open("config.txt", "r") as f:
	lines = f.readlines()
	for x in lines:
		print x
	print(f.readlines())