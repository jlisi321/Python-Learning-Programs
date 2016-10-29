import math

runProgram = True

while(runProgram == True):
	print("\npyTriple")
	print("Enter the length of your side(if the side is unknown enter 0)")
	sideA = int(input("Enter side A: "))
	sideB = int(input("Enter side B: "))
	sideC = int(input("Enter side C: "))

	if(sideA == 0):
		sideA = (sideC ** 2) - (sideB ** 2)
		sideA = math.sqrt(sideA)
		print("Side A = " + str(sideA))
	elif(sideB == 0):
		sideB = (sideC ** 2) - (sideA ** 2)
		sideB = math.sqrt(sideB)
		print("Side B = " + str(sideB))
	elif(sideC == 0):
		sideC = (sideA ** 2) + (sideB ** 2)
		sideC = math.sqrt(sideC)
		print("Side C = " + str(sideC))
	else:
		print("ERROR")

	playAgain = "error"
	while(playAgain != "Y" and playAgain != "y" and playAgain != "N" and playAgain != "n"):
		playAgain = str(input("Would you like to enter another problem?(Y/N):"))
		if(playAgain == "Y" or playAgain == "y"):
			runProgram == True
		elif(playAgain == "N" or playAgain == "n"):
			runProgram = False
			print("Thanks for using the program!\n")
		else:
			print("ERROR: Invalid Answer")

