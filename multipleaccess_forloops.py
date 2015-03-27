import threading



def write1(i):
	f1 = open("data1.txt","a+")
	for i in range (100) :
		f1.write(str(i))
		f1.write("\n")
		i = i + 1
	f1.close()

def write2(j):
	f2 = open("data2.txt","a+")		
	for j in range (100) :
		f2.write(str(j))
		f2.write("\n")
		j = j + 2


def collect(i,j):
	f1 = open("data1.txt","a+")
	f2 = open("data2.txt","a+")		
	f3 = open("data3.txt","a+")
	for x in range (100):
		y = f1.read(1)
		z = f2.read(1)
		#print (f1.read(1), f2.read(1))
		f3. write (f1.read(1), f2.read(1))		
		#f3.write(f1.read(x))
		#f3.write(f2.read(x))
	f1.close()
	f2.close()
	f3.close()

threads = []
i = 0
j = 0

t1 = threading.Thread(target = write1, args = (i,))
t2 = threading.Thread(target = write2, args = (j,))
t3 = threading.Thread(target = collect, args = (i,j,))
threads.append(t1)
threads.append(t2)
threads.append(t3)
t1.start()
t2.start()
t3.start()


