# -*- coding: utf-8 -*-

app_port = 5000

device_name = None
check_interval = 30 # 两次检查间隔多长时间（单位:秒），默认是5分钟
connect_timeout = 10 # 通过网络连接目标硬盘录像机允许的时长

mail_smtp = None # (host, port, mail_account, mail_password, use_tls)
mail_receiver = None 

sms_api_key = None
sms_receiver = None