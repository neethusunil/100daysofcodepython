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

tools=[rock,paper,scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(tools[user_input])
print("Computer chose:")
comp_input = random.choice(tools)
print(comp_input)

if(user_input == 0):
    if(comp_input == scissors):
        print("you win")
    elif(comp_input == rock):
        print("Its a draw")
    else:
        print("you lose")

if(user_input == 1):
    if(comp_input == rock):
        print("you win")
    elif(comp_input == paper):
        print("Its a draw")
    else:
        print("you lose")

if(user_input == 2):
    if(comp_input == paper):
        print("you win")
    elif(comp_input == scissors):
        print("Its a draw")
    else:
        print("you lose")