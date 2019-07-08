from socket import *
import time
import RPi.GPIO as GPIO
import time

relay = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay, GPIO.OUT)

while (True):
	done = True;

	file = open('/sys/class/thermal/thermal_zone0/temp', 'r')
	temp = int(file.readline())
	file.close()

	#print(temp)

	if (temp >= 55000):
		GPIO.output(relay, GPIO.LOW)
		done = False
	else:
		GPIO.output(relay, GPIO.HIGH)


	while (done == False):
		time.sleep(20)

		file = open('/sys/class/thermal/thermal_zone0/temp', 'r')
		temp = int(file.readline())
		file.close()

		#print(temp)

		if (temp <= 35000):
			done = True

	GPIO.output(relay, GPIO.HIGH)

	time.sleep(60)

GPIO.output(relay, GPIO.HIGH)

GPIO.cleanup()
