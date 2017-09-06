raw_string = input("Enter your string : ")

myStringList = raw_string.split(' ')
print(myStringList)

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