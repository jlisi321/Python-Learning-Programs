run = True

while(run == True):
	item_Price = float(input("Enter Item Price:"))
	money_Given = float(input("Enter Money Given:"))

	change = round(money_Given - item_Price, 2)

	print("Change:" + str(change) + " dollars")