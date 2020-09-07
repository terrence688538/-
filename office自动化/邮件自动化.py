import smtplib                                      # smtp服务器
from smtplib import SMTP_SSL                        # 加密邮件防止被截获
from email.mime.text import MIMEText                # 构造邮件的正文
from email.mime.multipart import MIMEMultipart      # 把邮件的各个部分装在一起
from email.header import Header                     # 邮件标题、收件人等
from email.mime.application import MIMEApplication  # 可以加入附件

#登录邮箱部分
host_server='smtp.sina.com'                         # smtp服务器
sender_sina='terrencejzy@sina.com'                  # 账号
pwd='cebbcef6bed61fbc'                              # 这里应该是授权码而不是密码

#构造邮件部分
sender_sina_mail='terrencejzy@sina.com'             # 发件人邮箱
receiver='terrencejzy@sina.com'                     # 收件人邮箱
mail_title='Python办公自动化邮件'                    # 邮件标题
mail_content="您好，<p>这是使用python登录Sina邮箱发送的邮件的测试:</p><p><a href='https://www.python.org'>python</a></p>"              #正文

msg=MIMEMultipart()                                  # 初始化一个邮件
msg['Subject']=Header(mail_title,'utf-8')            # 邮件主题
msg['From']=sender_sina_mail                         # 发件人
msg['To']=Header('测试邮箱','utf-8')                  # 收件人
msg.attach(MIMEText(mail_content,'html','utf-8'))    # 邮件正文   plain是无格式的方式   attach就是添加
attachment=MIMEApplication(open('C:/Users/Mechrevo/Desktop/作业.docx','rb').read())  #附件
attachment.add_header('Content-Disposition','attachment',filename='作业改名字.docx')  #重命名 Content-Disposition设置attachment
msg.attach(attachment)
try:
    smtp=SMTP_SSL(host_server)                       # ssl登录
    smtp.set_debuglevel(0)                           # 关闭debuglevel0     1是开启
    smtp.ehlo(host_server)                           # 提示服务器准备链接，确定状态
    smtp.login(sender_sina,pwd)                      # 账号密码
    smtp.sendmail(sender_sina_mail,receiver,msg.as_string())
    smtp.quit()
    print('邮件发送成功')
except smtplib.SMTPException:
    print('无法发送邮件')


import zmail
server=zmail.server('terrencejzy@sina.com','cebbcef6bed61fbc')
mail=server.get_latest()
zmail.show(mail)
print(mail['Subject'])
print(mail['id'])
print(mail['from'])
print(mail['to'])
print(mail['content_text'])
print(mail['content_html'])

zmail.save_attachment(mail,target_path=None,overwrite=True)       #target是储存的路径   overwrite是说如果有同名文件怎么办