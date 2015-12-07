# !/usr/bin/python
# -*- coding: <utf-8> -*-

list99 = []
with open("99.txt", "r") as f99:
	lines = f99.readlines()
	for x in lines:
		tmp = x.replace("\n", "")
		list99.append(tmp)

list51 = []
with open("51.txt", "r") as f51:
	lines = f51.readlines()
	for x in lines:
		tmp = x.replace("\n", "")
		list51.append(tmp)

print(list99)
print("============list99===========================================", len(list99))
print(list51)

payedIn51List = []
for x in list99:
	for y in list51:
		if(y == x):
			payedIn51List.append(y)

print("*************list99****************************************", len(list99))
print(list99)
print("*************payedIn51List****************************************", len(payedIn51List))
print(payedIn51List)
	