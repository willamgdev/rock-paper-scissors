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
#Write your code below this line 👇

import random

human_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"
    ))

computer_choice = random.randint(0, 2)
if human_choice == 0:
    print(rock)
    print(f'Computer chose: {computer_choice} \n')
    if computer_choice == 0:
        print('It\'s a draw')
    elif computer_choice == 1:
        print('You lose, try again.')
    elif computer_choice == 2:
        print('You win!!!!!.')
    
    
if human_choice == 1:
    print(paper)
    print(f'Computer chose: {computer_choice} \n')
    if computer_choice == 0:
        print('You win!!!!')
    elif computer_choice == 1 :
        print('It\'s a draw.')
    elif computer_choice == 2:
        print('You lose, try again.')
  
if human_choice == 2:
    print(scissors)
    print(f'Computer chose: {computer_choice} \n')
    if computer_choice == 0:
        print('You lose')
    elif computer_choice == 1 :
        print('You win !!!!.')
    elif computer_choice == 2:
        print('It\'s a draw .')


if computer_choice == 0:
  print(rock)
if computer_choice == 1:
  print(paper)
if computer_choice == 2:
  print(scissors)




