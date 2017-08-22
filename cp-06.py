raw_string = input("Enter your string : ")

#num_subString = raw_string.count(" ")

myStringList = raw_string.split(' ')
print(myStringList)
# myStringList = [0]*len(subString)
# for i in range(len(subString)):
#  	myStringList[i] = subString[i]

print (len(myStringList))
print ("Origin List: {}".format(myStringList))

Lists = myStringList
i = 0;
for eachList in Lists:
	if(len(eachList) < 3):
		del myStringList[i]
	i += 1

print ("After filered String: {}".format(myStringList))

print("After sorted: {}".format(sorted(myStringList)))