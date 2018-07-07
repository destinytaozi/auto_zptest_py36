# This file named sendmail.py
# His duty is to send email.
import smtplib
from email.mime.text import MIMEText
from email.header import Header
class sendmai():

    def send_mail(cls, SMTP_host, from_account, from_password, to_account, subject, content):
        # 1.实例化SMTP
        global msg_b, msg_all
        smtp = smtplib.SMTP()
        # 2. 链接邮件服务器
        smtp.connect(SMTP_host)
        # 3. 配置发送邮箱的用户名和密码
        smtp.login(from_account, from_password)
        # 4. 配置发送内容msg
        if type(content) == str:  # 如果content传参为一个字符串则返回这个字符串 否则（列表）则把列表数据传到html表中
            msg = MIMEText(content, 'plain', 'utf-8')
        else:
            msg_head = """
                       <table color="CCCC33" width="500" border="1" cellspacing="0" cellpadding="10" align="center">
                           <tr>
                             <td align="center">未生成销售or退货单的订单号</td>
                             <td align="center">单据状态</td>
                           </tr>   """
            msg_body = ""
            for i in range(len(content)):  # 遍历二阶列表
                msg_b = ''' <tr>   
                            <td align="center"> %s </td>
                            <td align="center"> %s </td> 
                            </tr>
                           ''' % (content[i][0], content[i][1])
                # print content[i][0], content[i][1]
                msg_body += msg_b  # 累加各个数值
            msg_all = msg_head + msg_body + '''</table>'''  # 组合表头跟表体
            msg = MIMEText(msg_all, 'HTML', 'utf-8')  # 拼接邮件内容
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = from_account
        msg['To'] = ','.join(to_account)
        # 5. 配置发送邮箱，接收邮箱，以及发送内容
        smtp.sendmail(from_account, to_account, msg.as_string())
        # 6. 关闭邮件服务
        smtp.quit()

    def montageStr(self, api_confirm, api_description):
        global msg_body, msg_b
        if api_confirm:
            msg_head = '''
                        <tr>
                         <td align="center">序号</td>
                         <td align="center">%s</td>
                         <td align="center">cid</td>
                         <td align="center">sheetid</td>
                        </tr>
                            ''' % (api_description)
            msg_body = ""
        # if len(api_confirm)>30:
        #    length_api=30
        #    for i in range(length_api):
        #        msg_b = '''
        #                 <tr>
        #                 <td align="center">%s</td>
        #                 <td align="center">%s</td>
        #                 <td align="center">%s</td>
        #                 </tr>
        #                ''' % (i,api_confirm[i][0], api_confirm[i][1])
        #        msg_body += msg_b
        #    msg_all = msg_head + msg_body
        # else:
            for i in range(len(api_confirm)):
                msg_b = '''
                        <tr>
                             <td align="center">%s</td>
                             <td align="center">%s</td>
                             <td align="center">%s</td>
                             <td align="center">%s</td>
                        </tr>
                        ''' % (i + 1, api_confirm[i][0], api_confirm[i][1], api_confirm[i][3])
                msg_body += msg_b
            msg_all = msg_head + msg_body
        else:
            msg_all = '''
                           <tr>
                             <td align="center" colspan = "4">%s</td>
                            </tr>
                       ''' % (api_description + "接口很干净，没有接口数据残留！")
        return msg_all

    def montageMsg(self, outconf, inconf, factoryConf, reGoodsConf, lossConf, stockAdjust):
        msg_head = '''
                  <table color = "CCCC33" width = "500" border = "1" cellspacing = "0" cellpadding = "10" align = "center" >
                    <tr>
                      <td align ="left" colspan ="4"><strong>WMS接口排查（按时间先后顺序）</strong></td>
                    </tr>        
              '''
        msg_tree = '''</table>'''
        msg_all = msg_head + outconf + reGoodsConf + inconf + factoryConf + lossConf + stockAdjust + msg_tree
        return msg_all
