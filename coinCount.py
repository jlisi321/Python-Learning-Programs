import math
print("Coin Counter")

#asking what the measurment will be
weight_type = int(input("Are you measuring in grams(1) or pounds(2):"))

#getting the weight of the coins
print("\nEnter the weight of the coins you have below")
pennies_weight = int(input("Pennies:"))
nickles_weight = int(input("Nickles: "))
dimes_weight = int(input("Dimes: "))
quarters_weight = int(input("Quarters: "))

#finding amount of coins
if(weight_type == 1):
	pennies_amount = math.floor(pennies_weight / 2.5)
	nickles_amount = math.floor(nickles_weight / 5.0)
	dimes_amount = math.floor(dimes_weight / 2.268)
	quarters_amount = math.floor(quarters_weight / 5.670)
elif(weight_type == 2):
	pennies_amount = math.floor(pennies_weight / 0.00551155)
	nickles_amount = math.floor(nickles_weight / 0.0110231)
	dimes_amount = math.floor(dimes_weight / 0.00500007816)
	quarters_amount = math.floor(quarters_weight / 0.0125001954)

#finding how many rolls you will need
pennies_rolls = math.ceil(pennies_amount / 50)
nickles_rolls = math.ceil(nickles_amount / 40)
dimes_rolls = math.ceil(dimes_amount / 50)
quarters_rolls = math.ceil(quarters_amount / 40)

#value of all there money
value = round((pennies_amount * .01) + (nickles_amount * .05) + (dimes_amount * .1) + (quarters_amount * .25), 2)

print("\nReport: ")
print("Amount of pennies:" + str(pennies_amount))
print("Rolls needed for pennies:" + str(pennies_rolls))

print("\nAmount of nickles:" + str(nickles_amount))
print("Rolls needed for nickles:" + str(nickles_rolls))

print("\nAmount of dimes:" + str(dimes_amount))
print("Rolls needed for dimes:" + str(dimes_rolls))

print("\nAmount of quarters:" + str(quarters_amount))
print("Rolls needed for quarters:" + str(quarters_rolls))

print("\nTotal Value of Money:" + str(value) + " dollars")

