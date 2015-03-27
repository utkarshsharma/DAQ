import json

with open("jsontest.txt") as json_file:
    json_data = json.load(json_file)
    print json_data
    x = json_data
    print x
    
#f = open ("jsonfile.txt","a+")
#f.write(str(x))
