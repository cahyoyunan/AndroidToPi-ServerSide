import RPi.GPIO as GPIO
import time
import os
import subprocess

#adjust for where your switch is connected
ldr1 = 27
ldr2 = 10
pir  = 17
mq5  = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(ldr1,GPIO.IN)
GPIO.setup(ldr2,GPIO.IN)
GPIO.setup(pir,GPIO.IN)
GPIO.setup(mq5,GPIO.IN)
prev_input1 = 0
prev_input2 = 0
prev_input3 = 0
prev_input4 = 0

print "Home Automation Berbasis Android dan Raspberry dengan Sistem Komunikasi melalui Wireless Local Area Network, Short Message Service Gateway dan Email "
print "==========By Cahyo Yunan Adianto (AndroidToPi)=============="
time.sleep(2)
print "==========Ready======"
print "\n"

while True:
  #assuming the script to call is long enough we can ignore bouncing
 input1=(not GPIO.input(27))
 input2=(not GPIO.input(10))
 input3= GPIO.input(17)
 input4= GPIO.input(22)


#LDR 1
 if ((not prev_input1) and input1):
        print "~~~~~~~~~~Lampu 1 nyala!~~~~~~~~~~"
	path = '/home/pi/smscenter/outbox/'
        print "~~~~~~~~~~harus kirim sms~~~~~~~~~"
        while True:
                if os.listdir(path) == []:
			print "~~~~~~~~~~SMS telah dikirim semua~~~~~~"
        	        subprocess.call(["sh", "/home/pi/bbt/ldr1on.sh"])
        	        subprocess.call(["python", "/home/pi/bbt/mailldr1on.py"])
			print "~~~~~~~~~~Email lampu 1 nyala telah dikirim semua~~~~~~"
               		time.sleep(5)
        		while True:
	                	if os.listdir(path) == []:
					print "~~~~~~~~~~SMS Berhasil Dikirim~~~~~~"
					print "\n"
					break
	                break
	#	break

 elif ( prev_input1 and (not input1)):
        print "~~~~~~~~~~Lampu 1 mati~~~~~~~~~~~"
	path = '/home/pi/smscenter/outbox/'
        print "~~~~~~~~~~harus kirim sms~~~~~~~~~"
        while True:
                if os.listdir(path) == []:
			print "~~~~~~~~~~SMS telah dikirim semua~~~~~~"
               		subprocess.call(["sh", "/home/pi/bbt/ldr1off.sh"])
        	        subprocess.call(["python", "/home/pi/bbt/mailldr1off.py"])
			print "~~~~~~~~~~Email lampu 1 mati telah dikirim semua~~~~~~"
                	time.sleep(5)
        		while True:
	                	if os.listdir(path) == []:
					print "~~~~~~~~~~SMS Berhasil Dikirim~~~~~~"
					print "\n"
					break
	                break
	#	break



#LDR2
 if ((not prev_input2) and input2):
        print "~~~~~~~~~~Lampu 2 nyala~~~~~~~~~~~"
	path = '/home/pi/smscenter/outbox/'
        print "~~~~~~~~~~harus kirim sms~~~~~~~~~"
        while True:
                if os.listdir(path) == []:
			print "~~~~~~~~~~SMS telah dikirim semua~~~~~~"
                	subprocess.call(["sh", "/home/pi/bbt/ldr2on.sh"])
        	        subprocess.call(["python", "/home/pi/bbt/mailldr2on.py"])
			print "~~~~~~~~~~Email lampu 2 nyala telah dikirim semua~~~~~~"
                	time.sleep(5)
        		while True:
	                	if os.listdir(path) == []:
					print "~~~~~~~~~~SMS Berhasil Dikirim~~~~~~"
					print "\n"
			                break
	                break

	#	break


 elif ( prev_input2 and (not input2)):
        print "~~~~~~~~~~Lampu 2 mati~~~~~~~~~~~"
	path = '/home/pi/smscenter/outbox/'
        print "~~~~~~~~~~harus kirim sms~~~~~~~~~"
        while True:
                if os.listdir(path) == []:
			print "~~~~~~~~~~SMS telah dikirim semua~~~~~~"
                	subprocess.call(["sh", "/home/pi/bbt/ldr2off.sh"])
        	        subprocess.call(["python", "/home/pi/bbt/mailldr2off.py"])
			print "~~~~~~~~~~Email lampu 2 mati telah dikirim semua~~~~~~"
                	time.sleep(5)
        		while True:
	                	if os.listdir(path) == []:
					print "~~~~~~~~~~SMS Berhasil Dikirim~~~~~~"
					print "\n"
				        break
		        break

	#	break



#PIR
 if ((not prev_input3) and input3):
	print("~~~~~~~~~~~Terdeteksi Motion~~~~~~~~~~~")
	path = '/home/pi/smscenter/outbox/'
        subprocess.call(["sh", "/home/pi/bbt/mailmotion.sh"])
        while True:
                if os.listdir(path) == []:
                        print "SMS telah dikirim semua"
                        time.sleep(3)
                        print "~~~~~~~~Harus kirim SMS~~~~~~~"
                        subprocess.call(["sh", "/home/pi/bbt/motiondaemon.sh"])
                        subprocess.call(["python", "/home/pi/bbt/gugelmotion.py"])
                        print "~~~~~~~~Email telah terkirim~~~~~~~"
                        time.sleep(5)

                        while True:
                                if os.listdir(path) == []:
		                        print "~~~~~~~~SMS telah terkirim~~~~~~~"
		                        time.sleep(10)
                                        print "~~~~~~~~Harus Telepon~~~~~~~~~"
                                        subprocess.call(["sh", "/home/pi/call.sh"])
                                        time.sleep(30)
                                        break

			print "\n"
			break



#MQ5
 if ( prev_input4 and (not input4)):
 	print ("~~~~~~~~~~~Terdeteksi Gas~~~~~~~~~~")
	path = '/home/pi/smscenter/outbox/'
        subprocess.call(["sh", "/home/pi/bbt/mailgas.sh"])
        while True:
                if os.listdir(path) == []:
                        print "SMS telah dikirim semua"
                        time.sleep(3)
                        print "~~~~~~~~Harus kirim SMS~~~~~~~"
                        subprocess.call(["sh", "/home/pi/bbt/gasdaemon.sh"])
                        subprocess.call(["python", "/home/pi/bbt/gugelgas.py"])
                        print "~~~~~~~~Email telah terkirim~~~~~~~"
                        time.sleep(5)

                        while True:
                                if os.listdir(path) == []:
		                        print "~~~~~~~~SMS telah terkirim~~~~~~~"
		                        time.sleep(10)
                                        print "~~~~~~~~Harus Telepon~~~~~~~~~"
                                        subprocess.call(["sh", "/home/pi/call.sh"])
                                        time.sleep(30)
                                        break

			print "\n"
			break


 #update previous input
 prev_input1 = input1
 prev_input2 = input2
 prev_input3 = input3
 prev_input4 = input4

 #slight pause to debounce
 time.sleep(3)


