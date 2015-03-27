import threading
import Adafruit_BBIO.ADC as ADC
import time
import json
from time import sleep
from time import gmtime, strftime

global adc0
global adc1
global adc2
global adc3
global adc4
global adc5
global uart1
global uart2
global uart4


ADC.setup()
UART.setup("UART1")
UART.setup("UART2")
UART.setup("UART4")


a0 = open("ADC0data.txt","a+")
a1 = open("ADC1data.txt","a+")
a2 = open("ADC2data.txt","a+")
a3 = open("ADC3data.txt","a+")
a4 = open("ADC4data.txt","a+")
a5 = open("ADC5data.txt","a+")
u1 = open("UART1data.txt","a+")
u2 = open("UART2data.txt","a+")
u4 = open("UART4data.txt","a+")
f = open("data.txt","a+")


def readADCs():
	while True:
		adc0 = ADC.read('AIN0')	
		a0.write(adc0)
		a0.write("\n")

		adc1 = ADC.read('AIN1')	
		a1.write(adc1)
		a1.write("\n")

		adc2 = ADC.read('AIN2')	
		a2.write(adc2)
		a2.write("\n")

		adc3 = ADC.read('AIN3')	
		a3.write(adc3)
		a3.write("\n")

		adc4 = ADC.read('AIN4')	
		a4.write(adc4)
		a4.write("\n")

		adc5 = ADC.read('AIN5')	
		a5.write(adc5)
		a5.write("\n")
		time.sleep(0.01)

#Ediff uC
def uart1():
        ser1 = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
        ser1.close()
	while True:
		ser1.open()
		if ser1.isOpen():
			uart1 = ser1.read(22)	# read 20 bytes excluding motor retrn parameters
			u1.write(uart1)
			u1.write("\n")
		ser1.close()
		time.sleep(0.01)


#GLV uC
def uart2():	
	ser2 = serial.Serial(port = "/dev/ttyO4", baudrate=9600)
	ser2.close()
	while True:
		ser2.open()
		if ser2.isOpen():
			uart2 = ser2.read(7)	# reads 5 bytes
			u2.write(uart2)
			u2.write("\n")
		ser2.close()
		time.sleep(0.01)

#BMS uC
def uart3():
	ser3.close()
	ser3 = serial.Serial(port = "/dev/ttyO2", baudrate=9600)
	while True:
		ser3.open()
		if ser3.isOpen():
			uart4 = ser3.read(5)	#need this values soon	#5 bytes
			u4.write(uart4)
			u4.write("\n")
		ser3.close()
		time.sleep(0.01)


def collect():
	while True:
		n = strftime("%a, %d %b %Y %X", gmtime())
		s = "$" + n + adc0 + adc1 + adc2 + adc3 + adc4 + adc5 + uart1[1] + uart1[2] + uart1[3] + uart1[4] + uart1[5] + uart1[6] + uart1[7] + uart1[8] + uart1[9] + uart1[10] + uart1[11] + uart1[12] + uart1[13] + uart1[14] + uart1[15] + uart1[16] + uart1[17] + uart1[18] + uart1[19] + uart1[20] + uart2[1] + uart2[2] + uart2[3] + uart2[4] + uart2[5] + uart4[1] + uart4[2] + uart4[3] + "#"
		
		f.write(s)
		f.write("\n")
		time.sleep(0.05)


threads = []


t = threading.Thread(target = readADCs)
threads.append(t)
#t.join()		#for serial execution
t1 = threading.Thread(target = uart1)
threads.append(t1)
t2 = threading.Thread(target = uart2)
threads.append(t2)
t3 = threading.Thread(target = uart3)
threads.append(t3)
t4 = threading.Thread(target = collect)
threads.append(t4)
t.start()
t1.start()
t2.start()
t3.start()
t4.start()