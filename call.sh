
#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back h$

chmod o+rw /dev/ttyUSB0
stty -F /dev/ttyUSB0 9600
echo -ne "ATDT 085880388574;" > /dev/ttyUSB0
