#coding = utf-8
#This file named test_demo.py
#his duty is to test some program.
from time import strptime
import datetime
from basic_func.do_mysql.mysql_con import doVsMySQL
import html
ss=datetime.datetime.now()
print(ss)
# print(strptime(ss, '%Y.%m.%d-%H:%M:%S'))

# Creates '<item size="large" quantity="6">Albatross</item>'
# def make_element(name,value,**attrs):
#     keyvlues=[' %s="%s"' % item for item in attrs.items()]
#     attr_str=''.join(keyvlues)
#     element='<{name}{attr_str}>{values}</{name}>'.format(
#         name=name,
#         attr_str=attr_str,
#         values=html.escape(value)
#     )
#     print(element)
#     return element
#
# make_element("item","Alibaba",size='large',quantity='6')

# def main():
#     return 1
#     # url='192.168.1.206'
#     # usrname='root'
#     # password='qazWSX098'
#     # dbBase='jianhu_zpwms'
#     # sql01="SELECT goodsName,planNumber,realNumber,unitName,barcode " \
#     #       "from t_stockout_plan_location WHERE batchCode='BCS001806060003' AND isDelete=0;"
#     # my_sql = doVsMySQL()
#     # sql_result=my_sql.query_close(url, usrname, password, dbBase, sql01)
#     # goodsid=[]
#     # goodsName=[]
#     # packingRate=[]
#     # planNumber=[]
#     # realNumber=[]
#     # unitName=[]
#     # barcode=[]
#     # print(sql_result)
#     # #把sql里查询到的多行值存到数值里
#     # for i in range(len(sql_result)):
#     #     goods_name,plan_number,real_number,unit_name,_ = sql_result[i]
#     #     goodsName.append(goods_name)
#     #     planNumber.append(plan_number)
#     #     realNumber.append(real_number)
#     #     unitName.append(unit_name)
#     #     print(goodsName[i],planNumber[i],realNumber[i],unitName[i])
#
#
# if __name__ == "__main__":
#     main()