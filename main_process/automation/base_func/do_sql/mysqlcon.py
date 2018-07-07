#This file named mysql_con.py
#His duty is to connect mysql datebase
import pymysql
pymysql.install_as_MySQLdb()

class doVsMySQL():
     def __init__(self):
         pass

     def connect_mysql(self, url, usrName, password, dbBase):
         #返回连接
         conn = pymysql.connect(url,usrName,password,dbBase,charset="utf8")
         print(dbBase," 已连接...")
         return conn

     def get_cursor(self, connect):
         #初始化并返回游标
         cursor = connect.cursor()
         return cursor

     def select_mysql(self, cursor, sql):
         #执行sql返回结果 关闭游标
         cursor.execute(sql)
         result = cursor.fetchall()
         cursor.close()
         return result

     def close_mysql(self, connect):
         connect.close()
         print("连接断开!")

     def mysql_query(self, url, usrName, password, dbBase, sql):
         #查询sql给出结果 并关闭连接
         conn = self.connect_mysql(url, usrName, password, dbBase)
         cursor = self.get_cursor(conn)
         result = self.select_mysql(cursor, sql)
         self.close_mysql(conn)
         return result