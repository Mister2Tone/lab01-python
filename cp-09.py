# f = open('./test.txt', 'w')
# f.write("AB\n")
# f.write("ZD\n")
# f.write("GH\n")
# f.close()

buffer = ''
file = open('./test.txt', 'r+')
for line in file:
	line = line.strip('\n')
	buffer += line

file.write(buffer)
file.close()
