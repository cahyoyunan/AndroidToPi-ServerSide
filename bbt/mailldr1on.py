import smtplib

fromaddr = 'raspiandrotopi@gmail.com'
toaddrs  = 'cahyoadianto10@gmail.com'
msg = 'Lampu 1 telah nyala!'


# Credentials (if needed)
username = 'raspiandrotopi'
password = 'Skyeats4airplane'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
