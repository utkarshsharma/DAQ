import threading
import Adafruit_BBIO.ADC as ADC

#ADC.setup()


def readADC(j):
	print "thread no", j 
	return
	#return(ADC.read(pin[j]))

#pin = []	
#pin[0] = 'AIN0'
#pin[1] = 'AIN1'
#pim[2] = 'AIN2'


threads = []

while True:
	for j in range(3):
		t = threading.Thread(target = readADC, args = (j,))
		threads.append(t)
		t.start()
		t.join()		#for serial execution

