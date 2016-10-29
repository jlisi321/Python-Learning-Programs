import random

print ("Guessing Game!(1-100)")

guessCheck = False
randomNumber = random.randrange(1, 100)
tries = 0

while(guessCheck == False):

	tries = tries + 1
	guess = int(input("Guess: "))

	if(guess == randomNumber):
		guessCheck = True
	else: 
		guessCheck = False

	if(guess < randomNumber):
		print ("You guessed too low!")
	elif(guess > randomNumber):
		print ("You guessed too high!")


print ("Good job you won in " + str(tries) + " tries!")