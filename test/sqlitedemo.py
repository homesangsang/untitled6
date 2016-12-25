# -*- coding: UTF-8 -*-
import sqlite
import student

conn = sqlite.connect("studentdbadmin.db")

print conn

cursor = conn.cursor()

def query(name):
    sql = "select * from stu_message where name= '" + name + "'"
    cursor.execute(sql)

    rs = cursor.fetchone()
    if rs:
        print rs[0]
        bishi = float(rs[1])
        shangji = float(rs[2])
        score = bishi + shangji
        if score < 120 :
            print "不及格"
        elif shangji < 60 :
            print "全部重考"
        elif bishi < 60 :
            print "笔试重考"
        else:
            print "考试通过!!!"

query("小明")
cursor.close()
conn.close()