my_List = [0]*5
for i in range(len(my_List)):
	my_List[i] = int(input("Enter #{0} :".format(i)))

result = 0
for i in range(len(my_List)):
	if(my_List[i] > 0):
		result += my_List[i]

print("My List is : {}".format(my_List))

print("result is : {}".format(result))