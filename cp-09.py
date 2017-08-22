# f = open('d:/test.txt', 'w')
# f.write("AB\n")
# f.write("ZD\n")
# f.write("GH\n")
# f.close()

f = open('d:/test.txt')
for line in f:
	print(line.strip('\n'), end="")
f.close()