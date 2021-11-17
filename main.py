print("Welcome to tips calculator!")
bill = float(input("What was the total bill?\n$"))  # converting str to float
tip = int(input("What percentage tip would you like to give? 10,12 or 15?\n"))  # converting str to int
people = int(input("How many people do you want to split the bill?\n"))
percentage = tip / 100
bill_percentage = bill * percentage
total = bill + bill_percentage
total_bill = total / people
# Format the result to 2 decimal places = 33.60
round1 = round(total_bill, 2)
print("Each person should pay:$" + str(round1))
