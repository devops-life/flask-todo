#!/usr/bin/env python
# encoding: utf-8


"""
@author: chenzhangpeng
@contact: chen_zhangpeng@163.com
@site: http://www.qinqinbaby.com
@file: create_sql.py
@time: 16/6/8 下午3:28
"""
import os
import datetime
#拼接sql语句
def sql_join():
    with open('link') as file:
        sqls = []
        for line in file.readlines():
            line = line.strip().split()
            sql = "insert into `qinqinbaby_2`.`legou_friend_link` ( `location`, `title`, `link_address`, `is_display`) values ( '1', '%s', '%s', '1');" % (line[0],line[1])
            sqls.append(sql)
        return sqls

#生成sql文件
def sql_file():
    file_name = time()+'.sql'
    if sql_file_isexists(file_name):
        with open(file_name,'w') as file:
            for sql in sql_join():
                file.write(sql+'\n')
    else:
        print "文件不存在"


#判断文件是否存在
def sql_file_isexists(file_name):
    filename = str(file_name)
    result = os.path.exists(filename)
    return result

#取得当前日期格式为YYYY-mm-dd
def time():
    now = datetime.datetime.now()
    curent_time = str(now)[0:10]
    return curent_time

#主程序
if __name__ == '__main__':
    sql_file()

