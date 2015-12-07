# !/usr/bin/python
# -*- coding: <utf-8> -*-

import mysql.connector

# 建立连接，拿到游标
conn = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", password="root", database="fcjiangDB", charset="utf8")
cursor = conn.cursor()

# 执行建表，插入数据
# cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
# cursor.execute("insert into user (id, name) values (%s, %s)", ("1", "fcjiang"))
# print("rowcount=%s", cursor.rowcount)

# 提交事务
conn.commit()
cursor.close()

# 查询操作
ssql = "select * from account"
cursor = conn.cursor()
cursor.execute(ssql)
# 遍历结果
allRecords = cursor.fetchall()
for item in allRecords:
	print("id=%s, name=%s, money=%s" % item)
cursor.close()


conn.close()
