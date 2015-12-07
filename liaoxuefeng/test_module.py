# !/usr/bin/python
# -*- coding: <utf-8> -*-

'a test module'

__author__ = "fcjiang"

import sys
from PIL import Image 

def test():
	args = sys.argv
	if len(args) == 1:
		print("hello world")
	elif len(args) == 2:
		print("hello %s" % args[1])
	else:
		print("too many args")

def use_pillow():
	myimg = Image.open("test.png")
	print(myimg.format, myimg.size, myimg.mode)
	myimg2 = myimg.thumbnail((200, 100))
	myimg2.save("thumb.jpg", "JPEG")

if __name__ == "__main__":
	test()
	print("=========================")
	use_pillow()