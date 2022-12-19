#coding=utf-8
import pymysql
'''
        code statue
        0   正常
        1   查询错误
        2   写入或更新错误
        3   删除错误
        4   未知错误
'''
def DBconnect():
    db = pymysql.connect(host="127.0.0.1", port=3306,user='root',password='srpihot*****666',database="GlobalCarban",charset='utf8')
    return db