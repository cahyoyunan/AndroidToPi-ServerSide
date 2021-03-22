import smtplib

fromaddr = 'raspiandrotopi@gmail.com'
toaddrs  = 'cahyoadianto10@gmail.com'
msg = 'Lampu 2 telah mati!'


# Credentials (if needed)
username = 'raspiandrotopi'
password = 'Skyeats4airplane'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
