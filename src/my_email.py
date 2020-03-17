import smtplib
from smtplib import SMTP
'''
阿里邮箱服务器:host_name="smtp.mxhichina.com",port = 25
'''

class MyEmail():
	"邮件发送"
	def __init__(self,host_name,port,user_name,passwd):
		self.host_name = host_name
		self.port = port
		self.user_name = user_name
		self.passwd = passwd
		
	def config_text_email(self,from_name,to_list,subject,text_msg):
		self.from_name = from_name
		self.to_list = ""
		for to in to_list:
			self.to_list += to + ","
		self.subject = subject
		self.text_msg = text_msg
		
		self.body = '\r\n'.join((      #组合sendmail方法的邮件主体内容，各段以"\r\n"进行分离
					"From: %s" %self.from_name,
                                        #"From: %s" %"admin",
					"TO: %s" %self.to_list,
					"subject: %s" %self.subject,
					"",
					self.text_msg
					))
		print(self.body)
	
	def send(self):
		try:
			server = SMTP()#创建一个smtp对象
			server.connect(self.host_name,str(self.port))
			server.login(self.user_name,self.passwd)
			server.sendmail(self.from_name,self.to_list,self.body)
			server.quit()
			print("成功向"+ self.to_list +"发送邮件")
			return True
		except smtplib.SMTPException:
			print ("Error: 无法发送邮件")
			return False
	
#HOST="smtp.mxhichina.com"  #定义smtp主机
#SUBJECT="test email form python"  #定义邮件主题
#TO = "pengyu@jht-design.com"   #定义邮件收件人
#FROM="jhtdesign@jht-design.com"  #定义邮件发件人
#text="python is test smtp"   #邮件内容,编码为ASCII范围内的字符或字节字符串，所以不能写中文
#BODY = '\r\n'.join((      #组合sendmail方法的邮件主体内容，各段以"\r\n"进行分离
#    "From: %s" %"admin",
#    "TO: %s" %TO,
#    "subject: %s" %SUBJECT,
#    "",
#    text
#))
#server = SMTP()   #创建一个smtp对象
#server.connect(HOST,'25')  #链接smtp主机
#server.login(FROM,"Jhtdesignteam01")  #邮箱账号登陆
#server.sendmail(FROM,TO,BODY) #发送邮件
#server.quit()  #端口smtp链接
