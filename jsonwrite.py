import json
myList = range(50,100)
for x in range (50):
	with open ('jsontest.txt','a+') as outfile: json.dump(myList[x],outfile)
	f = open ('jsontest.txt','a+')
	f.write('\n')
	f.close()



