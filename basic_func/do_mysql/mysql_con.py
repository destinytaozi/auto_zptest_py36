#This file named mysql_con.py
#His duty is to connect mysql datebase
import pymysql
pymysql.install_as_MySQLdb()

class doVsMySQL():
     def __init__(self):
         pass

     def con_mysql(self, url, usrName, password, dbBase):
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
         #cursor.close()
         return result

     def close_mycursor(self,cursor):
         cursor.close()
         print("游标关闭!")

     def close_mysql(self, connect,dbBase):
         connect.close()
         print("连接",dbBase,"断开!")

     def query_close(self, url, usrName, password, dbBase, sql):
         #查询sql给出结果 并关闭连接
         conn = self.con_mysql(url, usrName, password, dbBase)
         cursor = self.get_cursor(conn)
         result = self.select_mysql(cursor, sql)
         self.close_mycursor(cursor)
         self.close_mysql(conn,dbBase)
         return result