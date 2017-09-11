import operator

file = open('./employee.txt')
employeeDict = {}

for line in file:
	splitLine = line.split(':')
	employeeDict[splitLine[0]] = int(splitLine[1].strip('\n'))

file.close()

salarySorted = sorted(employeeDict.items(), key=operator.itemgetter(1), reverse=True )

print(employeeDict)
print("----------------")
print("Sum of salary: ",sum(employeeDict.values() ))
print("Salary by Ascending:")
employeeSortedDict = dict(salarySorted)
employeeName = list(employeeSortedDict.keys())
employeeSalary = list(employeeSortedDict.values())

for i in range(len(employeeName)):
	print(employeeName[i],":",employeeSalary[i])



