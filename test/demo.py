# -*- coding: UTF-8 -*-
from Tkinter import *
from tkMessageBox import *
import ttk
import sqlite
import sys

# 避免数据库中文乱码
reload(sys)
sys.setdefaultencoding('utf-8')
conn = sqlite.connect("studentdbadmin.db")

cursor = conn.cursor()


def check(character):
    for char in character:
        if not(char>= '0' and char<= '9'):
            showerror(title='错误提示', message='输入信息不合法')
            return 0
    return 1

def query(username):  # 查询学生信息
    if check(username) == 1:
        sql = "select * from stu_message where name= '" + username + "'"
        cursor.execute(sql)
        rs = cursor.fetchone()
        if rs:
            print rs[0]
            bishi = float(rs[1])
            shangji = float(rs[2])
            score = bishi + shangji
            if score < 120 :
                print "不及格"
                clearmessage()
                exam_res.insert(0, '不及格')
            elif shangji < 60 :
                print "全部重考"
                clearmessage()
                exam_res.insert(0, '全部重考')
            elif bishi < 60 :
                print "笔试重考"
                clearmessage()
                exam_res.insert(0, '笔试重考')
            else:
                print "考试通过!!!"
                clearmessage()
                exam_res.insert(0, '考试通过!!!')
            pass
        else:
            clearmessage()
            exam_res.insert(0, '数据库没有该考生的信息')




def insert(name, bishi, shangji):     # 插入一条记录
    sql = "insert into stu_message VALUES ('"+name+"',"+bishi+","+shangji+")"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
        showinfo("successful", "成功插入一条消息")
    except:
        # 如果执行不成功则回滚
        conn.rollback()


def clearmessage():      # 清楚表格中的信息
    uname_entry.delete(0, END)
    uname_input.delete(0, END)
    exam_res.delete(0, END)
    shangji_input.delete(0, END)
    bishi_input.delete(0, END)
    pass


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass


def hellobuttontest():  # 获取文本框(Entry)的值,获取学号和姓名
    uname_entry_value = uname_entry.get()
    print uname_entry_value
    query(uname_entry_value)


def insertrecord():
    uname = uname_input.get()
    shangji = shangji_input.get()
    bishi = bishi_input.get()
    if check(shangji) ==1 and check(bishi)==1:
        insert(uname, bishi, shangji)


root = Tk()
root.title('课程设计')
# root.geometry("800X600")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

ttk.Label(mainframe, text="用户名").grid(column=1, row=1, sticky=(W, E))
uname_entry = ttk.Entry(mainframe, width=10)
uname_entry.grid(column=2, columnspan=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="考试结果").grid(column=1, row=2, sticky=(W, E))
exam_res = ttk.Entry(mainframe, width=10, textvariable=feet)
exam_res.grid(column=2, columnspan=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="查询", command=hellobuttontest).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="重置", command=clearmessage).grid(column=3, row=3, sticky=W)

# 用户信息录入模块
ttk.Label(mainframe, text="用户信息录入").grid(column=1, row=4, columnspan=3, sticky=(W, E))

ttk.Label(mainframe, text="用户名").grid(column=1, row=5, sticky=(W, E))
uname_input = ttk.Entry(mainframe, width=10)
uname_input.grid(column=2, row=5, columnspan=2, sticky=(W, E))
ttk.Label(mainframe, text="笔试成绩").grid(column=1, row=6, sticky=(W, E))
bishi_input = ttk.Entry(mainframe, width=10)
bishi_input.grid(column=2, row=6, columnspan=2, sticky=(W, E))
ttk.Label(mainframe, text="上机成绩").grid(column=1, row=7, sticky=(W, E))
shangji_input = ttk.Entry(mainframe, width=10)
shangji_input.grid(column=2, row=7, columnspan=2, sticky=(W, E))
ttk.Button(mainframe, text="录入", command=insertrecord).grid(column=2, row=8, sticky=W)
ttk.Button(mainframe, text="重置", command=clearmessage).grid(column=3, row=8, sticky=W)


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
# pass_entry.focus()
root.mainloop()
