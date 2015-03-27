import threading


f1 = open("data1.txt","w+")
f2 = open("data2.txt","w+")
f3 = open("data3.txt","w+")

def write1(i):
	while True:
		f1.write(','.join(map(str,i)))
		#f1.write("\n")
		i = i + 1

def write2(j):
	while True:
		f1.write(','.join(map(str,j)))
		#f2.write("\n")
		j = j + 1

def collect(i,j):
	while True:
		f3.write(f1.read(1), f2.read(1))

threads = []
global i
global j
i = 0
j = 0

t1 = threading.Thread(target = write1, args = (i,))
t2 = threading.Thread(target = write2, args = (j,))
t3 = threading.Thread(target = collect)
threads.append(t1)
threads.append(t2)
threads.append(t3)
t1.start()
t2.start()
t3.start()


