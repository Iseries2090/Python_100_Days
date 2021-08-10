# import only system from os
import os
from art import logo


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


print(logo)
print("Welcome to the secret auction program.")
auction = {}
keep_going = "yes"
while keep_going == "yes":
    user = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: "))

    auction[user] = bid_amount
    keep_going = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

    #Clear screen doesn't seem to work, not sure the issue
    clear_screen()

current_winner = ""
current_highest = 0
for key in auction:
    if auction[key] > current_highest:
        current_winner = key
        current_highest = auction[key]

print(f"The winner is {current_winner} with a bid of {auction[current_winner]}")


