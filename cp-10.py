from urllib import request
import re

f = request.urlopen('http://fivedots.coe.psu.ac.th')
html = str(f.read().decode('utf-8'))
data = html.splitlines()
userList = data[32:77]

regex1 = r">(.*$)"
regex2 = r"^(\w.*\w\s\w.*)\s-->$"
regex3 = r">(.*\s.*)<"
regexText = r"\w.*\s.*\w$"

i=0
for user in userList:
	matches = re.findall(regex1,user)
	if re.match(regexText,matches[0]) :
		userList[i] = matches
	elif re.match(r"^\w.*\w\s\w.*\s-->$",matches[0]) :
		match2 = re.findall(regex2,matches[0])
		userList[i] = match2
	else:
		match3 = re.findall(regex3,matches[0])
		userList[i] = match3

	i+=1

print('-----------------Result-----------------')
for user in userList:
	print(user)