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
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
rpc = [rock, paper, scissors]
ran_choice = random.randint(0,2)



# if choice == ran_choice:
#     print("It's a Draw")
# elif choice == 0 and ran_choice == 1 or choice == 1 and ran_choice == 2 or choice == 2 and ran_choice == 0:
#     print("You Lose")
# else:
#     print("You Win")

if choice >= 0 and choice<= 2:
    print(rpc[choice])
    print("The Computer Chose:\n "
          f"{rpc[ran_choice]}")

if choice >= 0 and choice <= 2:
    if choice > ran_choice or choice == 0 and ran_choice == 2:
        print("You Win!")
    elif ran_choice > choice:
        print("You Lose!")
    else:
        print("It's a Draw.")
else:
    print("Enter a valid number")