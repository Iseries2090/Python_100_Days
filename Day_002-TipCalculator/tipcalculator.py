#Day 2 Project
#Tip Calculator

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
num_people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
tip_percent = tip / 100

bill = (total_bill * tip_percent) + total_bill / num_people
bill = "{:.2f}".format(bill)
print(f"Each person should pay: ${bill}")
