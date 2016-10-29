import time
import random
from Tkinter import *
root = Tk()
#setting window size
root.minsize(width=320, height=100)
root.maxsize(width=350, height=100)

#setting some global variables for the functions
loop = 0
playagain = 'y'

#Establishing libary
libary = {1: "It is certain", 2: "It is decidedly so", 3: "Without a doubt", 4: "Yes, definitely", 5: "You may rely on it",
6: "As I see it, yes", 7: "Most likely", 8: "Outlook good", 9: "Yes", 10: "Signs point to yes", 11: "Reply hazy try again",
12: "Ask again later", 13: "Better not tell you now", 14: "Cannot predict now", 15: "Concentrate and ask again", 
16: "Don't count on it", 17: "My reply is no", 18: "My sources say no", 19: "Outlook not so good", 20: "Very doubtful"}

#Putting framess in 
topFrame = Frame(root)
bottomFrame = Frame(root)
topFrame.pack(side=TOP)
bottomFrame.pack(side=BOTTOM)

play_again_label = Label(bottomFrame, text="Hit play again to be able to ask another question!")
randomAnswer = random.randint(1,20)
answer = Label(bottomFrame, text=libary[randomAnswer])


#Functions for buttons
def ask_function():
	global loop
	global answer
	global playagain
	global play_again_label
	global ask_question
	global text_box
	global randomAnswer
	global answer

	if(playagain == 'y'):
		if(loop >= 1):
			answer.grid_remove()

		randomAnswer = random.randint(1,20)
		answer = Label(bottomFrame, text=libary[randomAnswer])

		answer.grid(row = 0)
		loop = loop + 1
		playagain = 'n'
		ask_question.grid_remove()
		text_box.delete(0, 'end')
	elif(playagain == 'n'):
		answer.grid_remove()
		play_again_label.grid(row=0)

def clear_text_function():
	global text_box
	global answer
	text_box.delete(0, 'end')

def play_again_function():
	global playagain
	global play_again_label
	global text_box
	global answer
	playagain = 'y'
	play_again_label.grid_remove()
	text_box.delete(0, 'end')
	answer.grid_remove()

def quit_function():
	root.destroy()

#making buttons
ask = Button(topFrame, text= "Ask", command=ask_function)
clear_text = Button(topFrame, text="Clear Text", command=clear_text_function)
play_again = Button(topFrame, text= "Play Again", command=play_again_function)
quit = Button(topFrame, text="Quit", command=quit_function)

#placing titles
title = Label(topFrame, text= "Magic 8 Ball!")
title.grid(row=0, columnspan = 4)
ask_question = Label(bottomFrame, text="Ask me a question!")
ask_question.grid(row=0)

#placing buttons
ask.grid(row= 1, column= 0)
clear_text.grid(row= 1, column= 1)
play_again.grid(row= 1, column= 2)
quit.grid(row= 1, column= 3)

#making entry box
text_box = Entry(bottomFrame)
text_box.grid(row=1)
root.mainloop()