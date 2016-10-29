import math
print("Geometry Calculator!")

program_end = 2

#Function to check if the input was to end the program
def end_program(input, program_end):
	if(input == 0):
		program_end = 1


while(program_end == 2):

#Menu
	print("Enter Corresponding Number")
	print("1 - Square")
	print("2 - Circle")
	print("3 - Rectangle")
	print("4 - Rhombus")
	print("5 - Trapezium")
	print("6 - Parrellogram")
	print("0 - Ends program")
	shape = int(input("Enter Shape: "))
	end_program(shape, program_end)

#Checks what shape it is and then does the input for the calculations needed for finding the area
	if(shape == 1):
		width = int(input("Enter width: "))
		end_program(width, program_end)
		area = width * width
	elif(shape == 2):
		radius = int(input("Enter radius: "))
		end_program(radius, program_end)
		area = math.pi * (radius * radius)
	elif(shape == 3):
		length = int(input("Enter length: "))
		end_program(length, program_end)
		width = int(input("Enterwidth: "))
		end_program(width, program_end)
		area = length * width
	elif(shape == 4):
		a = int(input("Enter A: "))
		end_program(a, program_end)
		b = int(input("Enter B:"))
		end_program(b, program_end)
		area = a * b * .5
	elif(shape == 5):
		height = int(input("Enter height: "))
		end_program(height, program_end)
		base = int(input("Enter base length: "))
		end_program(base, program_end)
		top = int(input("Enter top length: "))
		end_program(top, program_end)
		area = 1/2 * (base + top) * height
	elif(shape == 6):
		base = int(input("Enter base: "))
		end_program(base, program_end)
		height = int(input("Enter height: "))
		end_program(height, program_end) 
		area = base * height
	elif(shape == 0):
		print("Bye Felicia")
	else: 
		print("ERROR - Invalid Choice")

#Prints the area 
	if(shape > 0 and shape <= 6):
		print("Area = " + str(area))






