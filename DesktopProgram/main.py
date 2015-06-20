import serial
ser = serial.Serial('/dev/rfcomm0', 9600)
while 1:
	string = ser.readline()
	print string
	#value = float(string)
	#print "Float: "
