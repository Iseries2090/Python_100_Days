import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_list = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0,2)

print(choice_list[player_choice])

print(f"Computer chose: \n {choice_list[computer_choice]}")

if player_choice == 0 and computer_choice == 2:
    print("You Win!")
elif player_choice == 1 and computer_choice == 0:
    print("You Win!")
elif player_choice == 2 and computer_choice == 1:
    print("You Win!")
else:
    print("You lose.")