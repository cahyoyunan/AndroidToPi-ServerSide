#!/bin/sh
from=$SMS_1_NUMBER
message=$SMS_1_TEXT
reply=""

#perintah lampu 1
if test "$message" = "Nyalakan lampu 1"; then
   sudo python /home/pi/smscenter/lampu1on.py
   reply="Lampu 1 telah nyala!"

elif test "$message" = "Matikan lampu 1"; then
     sudo python /home/pi/smscenter/lampu1off.py
     reply="Lampu 1 telah mati!"

#perintah lampu 2
elif test "$message" = "Nyalakan lampu 2"; then
   sudo python /home/pi/smscenter/lampu2on.py
   reply="Lampu 2 telah nyala!"

elif test "$message" = "Matikan lampu 2"; then
     sudo python /home/pi/smscenter/lampu2off.py
     reply="Lampu 2 telah mati!"

#perintah beban 1
elif test "$message" = "Nyalakan beban 1"; then
   sudo python /home/pi/smscenter/beban1on.py
   reply="Beban 1 telah nyala!"

elif test "$message" = "Matikan beban 1"; then
     sudo python /home/pi/smscenter/beban1off.py
     reply="Beban 1 telah mati!"

#perintah beban 2
elif test "$message" = "Nyalakan beban 2"; then
   sudo python /home/pi/smscenter/beban2on.py
   reply="Beban 2 telah nyala!"

elif test "$message" = "Matikan beban 2"; then
     sudo python /home/pi/smscenter/beban2off.py
     reply="Beban 2 telah mati!"


#help syntax
elif test "$message" = "Help"; then
     reply="Syntax yaitu 'Nyalakan atau Matikan' lampu '1/2'(no lampu)"


else
    reply="Salah syntax ? balas 'Help' untuk keterangan lebih lanjut"
fi

#echo "$reply" | sudo gammu sendsms TEXT "$from"
