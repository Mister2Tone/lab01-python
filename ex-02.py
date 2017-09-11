import os

file = open('./student.txt')
studentDict = {}

for line in file:
	splitLine = line.split('=')
	studentDict[splitLine[0]] = splitLine[1].strip('\n')

file.close()

studentId = list(studentDict.keys())
studentGroup = list(studentDict.values())

for i in range(len(studentId)):
	dirName = studentId[i]
	group = studentGroup[i]

	rootDir = os.getcwd()

	if os.path.isdir(dirName) :
		os.chdir(dirName)
	else :
		os.mkdir(dirName)
		os.chdir(dirName)

	checkDir = ("{0}\{1}".format(rootDir,dirName))

	if(os.getcwd() == checkDir):
		file = open("work.conf", "w")
		file.write("id={0}\n".format(dirName))
		file.write("group={0}\n".format(group))
		file.close()
		os.chdir("..")
	else:
		print("wrong, please check your path directory")
