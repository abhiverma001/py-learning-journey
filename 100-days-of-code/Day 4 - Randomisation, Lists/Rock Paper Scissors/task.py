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


image = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors : "))
if user_choice >= 0 and user_choice <= 2:
    print(image[user_choice])

computer_choice = random.randint(0, 2)
print(image[computer_choice])
#
# if user_choice == computer_choice:
#     print("retry")
# elif user_choice > 2 or user_choice < 0 :
#     print("invalid number!")
# elif user_choice < computer_choice:
#     print("You win!")
# elif user_choice == 1 and 0 == computer_choice == 2 :
#     print("You lose!")
# elif user_choice == 2 and computer_choice == 1 :
#     print("You win!")
# elif user_choice == 2 and computer_choice == 0 :
#     print("You loose!")
