import serial

ser = serial.Serial('/dev/ttyAMA0',9600)

while True:
	x=ser.readline()
	print x
