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

def readADC():
	while True:
		a0 = open("ADC0data.txt","a+")
		a0.write(ADC.read('AIN0'))
		a0.close()

def uart1():
        ser1 = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
        ser1.close()
        for x in range(100):
                ser1.open()
                if ser1.isOpen():
                #print "Serial1 is open!"
                #ser1.write("x")
                        print "UART1", ser1.read()
                ser1.close()
        return

def uart2():
        ser2 = serial.Serial(port = "/dev/ttyO4", baudrate=9600)
        ser2.close()
        for y in range(100):
                ser2.open()
                if ser2.isOpen():
                #print "Serial2 is open!"
                #ser2.write("y")
                        print "UART4", ser2.read()
                ser2.close()
        return

def uart3():
        ser3 = serial.Serial(port = "/dev/ttyO2", baudrate=9600)
        ser3.close()
        for i in range(100):
                ser3.open()
                if ser3.isOpen():
                #print "Serial3 is open!"
                #ser3.write("c")
                        print "UART2", ser3.read()
                ser3.close()
        return


def collect(i,j):
		while True:
		u1 = open("UART1data.txt","r+")
		u2 = open("UART2data.txt","r+")		
		u3 = open("UART4data.txt","r+")
		a0 = open("ADC0data.txt","r+")
		a1 = open("ADC1data.txt","r+")
		a2 = open("ADC2data.txt","r+")
		a3 = open("ADC3data.txt","r+")
		a4 = open("ADC4data.txt","r+")
		a5 = open("ADC5data.txt","r+")
		
		n = strftime("%a, %d %b %Y %X", gmtime())
		s1 = u1.read(1)
		s2 = u2.read(1)
		s3 = u3.read(1)
		s4 = a0.read(1)
		s5 = a1.read(1)
		s6 = a2.read(1)
		s7 = a3.read(1)
		s8 = a4.read(1)
		s9 = a5.read(1)
		s10 = a6.read(1)
		
		#print (f1.read(1), f2.read(1))
		#f3. write (f1.read(1), f2.read(1))		
		#f3.write(f1.read(1))
		#f3.write(f2.read(1))
		f1.close()
		f2.close()
		f3.close()
		time.sleep(0.01)


threads = []

t = threading.Thread(target = readADC)
threads.append(t)
#t.join()		#for serial execution
t1 = threading.Thread(target = uart1)
threads.append(t1)
t2 = threading.Thread(target = uart2)
threads.append(t2)
t3 = threading.Thread(target = uart3)
threads.append(t3)
t.start()
t1.start()
t2.start()
t3.start()

