def print_lyrics(number):
	if(number > 1):
		print str(number) + " bottles of beer on the wall, " + str(number) + " bottles of beer."
	elif(number == 1):
		print str(number) + " bottle of beer on the wall, " + str(number) + " bottle of beer."
	number = number - 1
	print 
	if(number > 0):
		print "Take one down and pass it around, " + str(number) + " bottles of beer on the wall."
	elif(number == 0):
		print "Take one down and pass it around, no more bottles of beer on the wall."
	print

beer_number = 99

while(beer_number > 1):
	print_lyrics(beer_number)
	beer_number = beer_number - 1

print "No more bottles of beer on the wall, no more bottles of beer."
print
print "Go to the store and buy some more, 99 bottles of beer on the wall."
