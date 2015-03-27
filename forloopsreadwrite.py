f1 = open("d1.txt","w+")
f2 = open("d2.txt","w+")


for i in range(100):
	f1.write(str(i))
	#if i != 99:
		#f1.write(',')
	f1.write("\n")
	i = i + 1
	
for j in range(100):
	f2.write(str(j))
	#if j != 99:
		#f2.write(',')
	f2.write("\n")
	j = j + 1
	
f1 = open("d1.txt","w+")
f2 = open("d2.txt","w+")
f3 = open("d3.txt","w+")

for x in range (199):
	#print (f1.read(x))
	#print (f2.read(x))
	f3.write((f1.read(x)))
	f3.write((f2.read(x)))

