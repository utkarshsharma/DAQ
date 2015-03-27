import threading
import Adafruit_BBIO.ADC as ADC
import time
import json
from time import sleep
from time import gmtime, strftime

ADC.setup()
UART.setup("UART1")
UART.setup("UART2")
UART.setup("UART4")

def readADCs():
	while True:
		a0 = open("ADC0data.txt","a+")
		a0.write(ADC.read('AIN0'))
		a0.close()

		a1 = open("ADC1data.txt","a+")
		a1.write(ADC.read('AIN1'))
		a1.close()

		a2 = open("ADC2data.txt","a+")
		a2.write(ADC.read('AIN2'))
		a2.close()

		a3 = open("ADC3data.txt","a+")
		a3.write(ADC.read('AIN3'))
		a3.close()

		a4 = open("ADC4data.txt","a+")
		a4.write(ADC.read('AIN4'))
		a4.close()

		a5 = open("ADC5data.txt","a+")
		a5.write(ADC.read('AIN5'))
		a5.close()
	time.sleep(0.01)

def uart1():
        ser1 = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
        ser1.close()
	while True:
		ser1.open()
		if ser1.isOpen():
		#print "Serial1 is open!"
		#ser1.write("x")
			with open('UART1.txt','a+') as outfile: json.dump(ser1.read(),outfile)
		ser1.close()
	time.sleep(0.01)

def uart2():
	ser2 = serial.Serial(port = "/dev/ttyO4", baudrate=9600)
	ser2.close()
	while True:
		ser2.open()
		if ser2.isOpen():
		#print "Serial2 is open!"
		#ser2.write("y")
			with open('UART4.txt','a+') as outfile: json.dump(ser2.read(),outfile)
		ser2.close()
	time.sleep(0.01)

def uart3():
	ser3 = serial.Serial(port = "/dev/ttyO2", baudrate=9600)
	ser3.close()
	while True:
		ser3.open()
		if ser3.isOpen():
		#print "Serial3 is open!"
		#ser3.write("c")
			with open('UART2.txt','a+') as outfile: json.dump(ser3.read(),outfile)
		ser3.close()
	time.sleep(0.01)


def collect():
	while True:
		u1 = open("UART1data.txt","a+")
		u2 = open("UART2data.txt","a+")		
		u3 = open("UART4data.txt","a+")
		a0 = open("ADC0data.txt","a+")
		a1 = open("ADC1data.txt","a+")
		a2 = open("ADC2data.txt","a+")
		a3 = open("ADC3data.txt","a+")
		a4 = open("ADC4data.txt","a+")
		a5 = open("ADC5data.txt","a+")
		
		n = strftime("%a, %d %b %Y %X", gmtime())
		s1 = u1.read(1)		#adjust the no of bytes to be read
		s2 = u2.read(1)		#adjust the no of bytes to be read
		s3 = u3.read(1)		#adjust the no of bytes to be read
		s4 = a0.read(2)		#ADC reading accuracy of 12 bits
		s5 = a1.read(2)
		s6 = a2.read(2)
		s7 = a3.read(2)
		s8 = a4.read(2)
		s9 = a5.read(2)
		s10 = a6.read(2)
		
		u1.close()
		u2.close()
		u3.close()
		a0.close()
		a1.close()
		a2.close()
		a3.close()
		a4.close()
		a5.close()
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

