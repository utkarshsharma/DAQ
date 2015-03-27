from threading import Thread
import urllib
import re

def geturl(url):
	base = "http://finance.yahoo.com/q?s" + url
	regex = '<span id>=''yfs_184_'+ url +' ''>(.+?)</span>'
	pattern = re.compile(regex)
	htmltext = urllib.urlopen(base).read()
	results = re.findall(pattern, htmltext)
	print "the price of ", url, " is ", results

symbolslist = open ("symbols.txt").read()

symbolslist = symbolslist.split(",")

threadlist = []

for u in symbolslist:
	t = Thread(target = geturl, args = (u,))
	t.start()
	threadlist.append(t)

for a in threadlist:
	a.join()
