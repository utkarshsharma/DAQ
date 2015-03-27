import threading
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.ADC as UART
import time
import serial
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
UART.setup('UART1')
UART.setup('UART2')
UART.setup('UART4')
global x
x = serial.Serial("/dev/ttyUSB0",baudrate =9600)

#a0 = open("ADC0data.txt","a+")
#a1 = open("ADC1data.txt","a+")
#a2 = open("ADC2data.txt","a+")
#a3 = open("ADC3data.txt","a+")
#a4 = open("ADC4data.txt","a+")
#a5 = open("ADC5data.txt","a+")
#u1 = open("UART1data.txt","a+")
#u2 = open("UART2data.txt","a+")
#u4 = open("UART4data.txt","a+")
f = open("data.txt","a+")

def readADCs():
        while True:
                a0 = open("ADC0data.txt","a+")
                a1 = open("ADC1data.txt","a+")
                a2 = open("ADC2data.txt","a+")
                a3 = open("ADC3data.txt","a+")
                a4 = open("ADC4data.txt","a+")
                a5 = open("ADC5data.txt","a+")

                adc0 = ADC.read('AIN0')
                a0.write(str(adc0))
                a0.write("\n")

                adc1 = ADC.read('AIN1')
                a1.write(str(adc1))
                a1.write("\n")

                adc2 = ADC.read('AIN2')
                a2.write(str(adc2))
                a2.write("\n")

                adc3 = ADC.read('AIN3')
                a3.write(str(adc3))
                a3.write("\n")

                adc4 = ADC.read('AIN4')
                a4.write(str(adc4))
                a4.write("\n")

                adc5 = ADC.read('AIN5')
                a5.write(str(adc5))
                a5.write("\n")
                time.sleep(0.1)

                a0.close()
                a1.close()
          
                          a2.write("\n")

                adc3 = ADC.read('AIN3')
                a3.write(str(adc3))
                a3.write("\n")

                adc4 = ADC.read('AIN4')
                a4.write(str(adc4))
                a4.write("\n")

                adc5 = ADC.read('AIN5')
                a5.write(str(adc5))
                a5.write("\n")
                time.sleep(0.1)

                a0.close()
                a1.close()
                a2.close()
                a3.close()
                a4.close()
                a5.close()

#Ediff uC
def uart1():
        ser1 = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
        ser1.close()
        while True:
                u1 = open("UART1data.txt","a+")
                ser1.open()
                if ser1.isOpen():
                        uart1 = ser1.read(5)    # read 20 bytes excluding motor retrn parameters
                        u1.write(str(uart1))
                        u1.write("\n")
                        i = ord(uart1[1])
                        x.write(uart1)
                ser1.close()
               u1.close()
                time.sleep(0.01)


#GLV uC
def uart2():
        ser2 = serial.Serial(port = "/dev/ttyO2", baudrate=9600)
        ser2.close()
        while True:
                u2 = open("UART2data.txt","a+")
                ser2.open()
                if ser2.isOpen():
                        uart2 = ser2.read(7)    # reads 5 bytes
                        u2.write(str(uart2))
                        u2.write("\n")
                ser2.close()
                u2.close()
                time.sleep(0.01)

#BMS uC
def uart3():
        ser3 = serial.Serial(port = "/dev/ttyO4", baudrate=9600)
        ser3.close()
        while True:
                u4 = open("UART4data.txt","a+")
                ser3.open()
                if ser3.isOpen():
                        uart4 = ser3.read(5)    #need this values soon  #5 bytes
                        u4.write(str(uart4))
                        u4.write("\n")
                ser3.close()
                u4.close()
                time.sleep(0.01)


def collect():
        while True:
                n = strftime("%a, %d %b %Y %X", gmtime())
                                            s = "$"
                s.append(n)
                s.append(uart1)
                # n + str(adc0) + str(adc1) + str(adc2) + str(adc3) + str(adc4) + str(adc5) + uart1[1] + uart1[2] + uart1[3] + uart1[4] + uart1$
                f.write(s)
                f.write("\n")
                #Xbee sending part
                x.write(s)
                print s
                time.sleep(0.01)


threads = []


t = threading.Thread(target = readADCs)
threads.append(t)
#t.join()               #for serial execution
t1 = threading.Thread(target = uart1)
threads.append(t1)
t2 = threading.Thread(target = uart2)
threads.append(t2)
t3 = threading.Thread(target = uart3)
threads.append(t3)
t4 = threading.Thread(target = collect)
threads.append(t4)
#t.start()
t1.start()
#t2.start()
#t3.start()
#t4.start()


                                 
