import math

def bmi(weight,height):
	height = height/100
	return (weight/pow(height,2))

def docterComment(bmi):
	comment = ""
	if bmi > 40 :
		comment = "Maximum fat level"
	elif (bmi > 35.0) and (bmi < 39.9) :
		comment = "Fat level 2"
	elif (bmi > 28.5) and (bmi < 34.9) :
		comment = "Fat level 1"
	elif (bmi > 23.5) and (bmi < 28.4) :
		comment = "Overweight"
	elif (bmi > 18.5) and (bmi < 23.4) :
		comment = "Normal"
	else :
		comment = "Underweight"
	return comment


name =       input("Please enter your name   : ")
weight = int(input("Your weight (Kilogram)   : "))
height = int(input("Your height (Centimetre) : "))

bmi = bmi(weight,height)
comment = docterComment(bmi)

file = open('./Report.txt', 'w')
file.write("================Result==============\n")
file.write("Your Name          : {0}\n".format(name) )
file.write("Your BMI           : {0:.2f}\n".format(bmi) )
file.write("The doctor mention : {0}\n".format(comment) )
file.write("====================================\n")

file.close()
