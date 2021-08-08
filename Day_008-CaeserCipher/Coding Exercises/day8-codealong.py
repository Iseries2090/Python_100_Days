#Review
#Create a fcuntion called greet()
#Write 3 print statements inside the function
#Call the greet() function and run your code

# def greet():
#     print("Hello.")
#     print("How are you today?")
#     print("Have a great day!")
# greet()

#Function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
# greet_with_name("Kyle")

#functions with more than 1 input
# def greet_with(name, location):
#     print(f"Hello, {name}.")
#     print(f"What is it like in {location}?")
# # greet_with("Kyle","St. Charles")
#
# #functions with keyword arguments
# greet_with(location="Indiana",name="Kyle")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(text,shift):
#     cipher_txt = ""
#     for num in range(len(text)):
#         index = alphabet.index(text[num])
#         cipher_txt += alphabet[index + 5]
#
#
#     print(cipher_txt)
#
#
# encrypt(text="hello",shift=5)

list = ["fighter", "black mage", "white mage", "black belt", "thief"]
import random
def final_party():
    party = []
    for num in range(4):
        party.append(random.choice(list))
    print(party)
final_party()
