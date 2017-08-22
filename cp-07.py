raw_string = input("Enter your string : ")

myStringList = raw_string.split(' ')

# print (len(myStringList))
print("Origin List: {}".format(myStringList))

LenStringList = [0]*len(myStringList)
for i in range(len(LenStringList)):
	LenStringList[i] = len(myStringList[i])

myDict = {}
for i in range(len(myStringList)):
	myDict[myStringList[i]] = LenStringList[i]

print(myDict)

value, key = max((value,key) for key,value in myDict.items())
print("This input has max value is {}".format(key))
	