#!/bin/sh
from=$SMS_1_NUMBER
message=$SMS_1_TEXT
reply=""

#perintah lampu 1
if test "$message" = "Nyalakan lampu 1"; then
    reply="Lampu 1 telah nyala!"
    python /home/pi/coba.py

elif test "$message" = "Matikan lampu 1"; then
    reply="Lampu 1 telah mati!"
    python /home/pi/coba2.py


#help syntax
elif test "$message" = "Help"; then
    reply="Syntax yaitu 'Nyalakan atau Matikan' lampu '1/2'(no lampu)"


else
    reply="Salah syntax ? balas 'Help' untuk keterangan lebih lanjut"
fi

echo "$reply" | sudo gammu-smsd-inject TEXT "$from"
