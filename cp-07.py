raw_string = input("Enter your string : ")

myStringList = raw_string.split(' ')

myDict = dict( (key, len(key)) for key in myStringList )

value, key = max((value,key) for key,value in myDict.items())
print("This input has max value is {}".format(key))
	