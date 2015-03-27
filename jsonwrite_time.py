
from time import gmtime, strftime

import json
x= 0
while(True):
	data = []
	y = strftime("%a, %d %b %Y %X", gmtime())
	print str(x/9)+y
	data.append(str(x/9)+y)
	with open('data2.txt', 'a') as outfile:	json.dump(data, outfile)
	x = x+1
