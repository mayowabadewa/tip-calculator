total = float(input("Welcome to the tip calculator.\n What was the total bill? $"))
tip = float(input("What percentage tip will you like to give?"))
number_of_persons = int(input("How many people should split the bill?"))

tip_percent = (tip / 100) + 1
new_total = total * tip_percent
amount = "{:.2f}".format((new_total / number_of_persons))
print(f"Each person should pay: ${amount}")
