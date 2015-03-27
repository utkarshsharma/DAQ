import Adafruit_BBIO.UART as UART
import serial
import threading

UART.setup("UART1")
UART.setup("UART4")
UART.setup("UART2")


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

threads = []

t1 = threading.Thread(target = uart1)
threads.append(t1)
t2 = threading.Thread(target = uart2)
threads.append(t2)
t3 = threading.Thread(target = uart3)
threads.append(t3)
t1.start()
t2.start()
