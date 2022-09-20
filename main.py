#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
total = float(input("Welcome to the tip calculator.\n What was the total bill? $"))
tip = float(input("What percentage tip will you like to give?"))
number_of_persons = int(input("How many people should split the bill?"))

tip_percent = (tip / 100) + 1
new_total = total * tip_percent
amount = "{:.2f}".format((new_total / number_of_persons))
print(f"Each person should pay: ${amount}")