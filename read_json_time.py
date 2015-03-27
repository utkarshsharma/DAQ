import json

with open("data2.txt") as json_out1:
	json_data1 = json.load(json_out1)
with open("data2.txt") as json_out2:
	json_data2 = json.load(json_out2)
for i in range (100):
	x = json_data1[i],json_data2[i]
	#print (x)
	with open('data3.txt', 'a+') as outfile3:json.dump(x, outfile3)
	

