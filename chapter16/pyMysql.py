# -*- coding:utf-8 -*-

__author__ = 'hzliyong'

import pymysql

db = pymysql.connect('localhost', 'root', 'root', 'python')
cursor = db.cursor()

cursor.execute("select version()")
data = cursor.fetchone()
print('Database version: %s ' % data)

cursor.execute("insert into people (name, age, sex) values ('Jee', 21, 'F') ")
r = cursor.execute("delete from people where age = 20")
db.commit()

r = cursor.execute('select * from people')
r = cursor.fetchall()
print(r)

cursor.close()
db.close()