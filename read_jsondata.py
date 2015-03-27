import json

with open("data1.txt") as json_out1:
	json_data1 = json.load(json_out1)
with open("data2.txt") as json_out2:
	json_data2 = json.load(json_out2)

	x = json_data1,json_data2
	#print (x)

with open('data3.txt', 'a') as outfile3:json.dump(x, outfile3)

