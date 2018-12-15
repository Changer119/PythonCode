#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 获取当前日期-时间2222
# import time
# nowDate = time.strftime('%Y-%m-%d')
# nowTime = time.strftime('%H:%M:%S')
# print nowDate
# print nowTime

# ******************************************************************************

# 列表去重（List去重）
# lst = [(1, 'fcjiang'), (2, 'fcjiang'), (3, 'sszhu'), (1, 'fcjiang')]
# print lst
# s = set(lst)
# print s
# lst2 = [1, 2, 3, 1, 2, 4, 5, 6]
# print lst2
# s2 = set(lst2)
# print s2

# *******************************************************************************
# 列表排序（List排序）
# a = [('2011-03-17', '2.26', 6429600, '0.0'), ('2011-03-16', '2.26', 12036900, '-3.0'), ('2011-03-15', '2.33', 15615500,'-19.1')]
# print a[0][0]
# b = sorted(a, key=lambda result: result[1], reverse=True)
# print b
# c = sorted(a, key=lambda result: result[2], reverse=True)
# print c
# dd = [2, 4, 3, 7, 5]
# ddd = sorted(dd)
# print ddd

# *******************************************************************************
# 遍历目录
# import os
# fileList = []
# s = os.sep  #根据unix或者windows系统不同，代表/或者\
# root = "E:" + s + "Code" + s	# 要查询的根目录是E:\Github
# print root

# # 熟悉os.walk()返回的值
# walk_result = os.walk(root)
# for x in walk_result:
# 	print x
# print '*************'

# # 遍历文件
# for rt, dirs, files in os.walk(root):
#     for f in files:
#         fname = os.path.splitext(f)
#         firt_part = fname[0]
#         length = len(firt_part)
#         new = firt_part[0:length-2] + fname[1]
#         os.rename(os.path.join(rt,f), os.path.join(rt,new))


# *******************************************************************************
# 字典排序(dict sort) 根据value排序
# from operator import itemgetter
# aa = {"a":"1","sss":"2","ffdf":'5',"ffff2":'3'}
# sort_aa = sorted(aa.items(), key=itemgetter(1))
# print sort_aa

# *******************************************************************************
# 字典-->字符串
# obj = {'name':'fcjiang', 'age':28, 'cellphone':'13567115159'}
# lst = []
# for k, v in obj.items():
# 	s = '%s=%s' %(k, v)
# 	lst.append(s)
# string_obj = ';'.join(lst)
# print string_obj



# *******************************************************************************
# 字符串-->字典
# a = 'server=mpilgrim;uid=sa;database=master;pwd=secret'
# aa = {}
# for i in a.split(';'):
# 	kv = i.split('=')
# 	aa[kv[0]] = kv[1]
# print aa

# *******************************************************************************
# 进制转换
# num = 16
# print 'Hex=%x, Dec=%d, Oct=%o' %(num, num, num)

# *******************************************************************************
# 调用系统命令或者脚本
import os
# 使用 os.system() 调用系统命令 , 程序中无法获得输出和返回值
print os.system('dir')
print '*******************'
# 使用 os.popen() 调用系统命令, 程序中可以获得命令输出，但是不能得到执行的返回值
out = os.popen("dir")
print out.read()
print '*******************'

