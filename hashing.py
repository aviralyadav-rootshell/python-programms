"""import smtplib
fromaddr = 'fromuser@gmail.com'
toaddrs  = 'touser@gmail.com'
msg = 'Enter you message here'
server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(username,password)
server.login(username,password)"""


import smtplib


fromaddr = 'hacker@gmail.com'
toaddrs  = 'adityamalikgupta285@gmail.com'


msg = 'hiiii'

username = 'blackhatal@gmail.com'
password = 'LpJt2HK4@&Evgl'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
print("hiii")
