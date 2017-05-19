import serial
import os

os.system("ls /dev | grep ttyA")

print "Potential inputs:"
print "1. ACM0"
print "2. AMA0"
print ""

option = str(raw_input("Please choose input: "))

if option==str(1):
	ser = serial.Serial('/dev/ttyACM0',9600)
elif option==str(2):
	ser = serial.Serial('/dev/ttyAMA0',9600)

while True:
	x=ser.readline()
	print x
