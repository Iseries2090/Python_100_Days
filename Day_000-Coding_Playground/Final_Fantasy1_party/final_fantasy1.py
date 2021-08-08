import random


list = ["fighter", "black mage", "white mage", "black belt", "thief"]


def final_party():
    party = []
    for num in range(4):
        party.append(random.choice(list))
    print(party)

final_party()