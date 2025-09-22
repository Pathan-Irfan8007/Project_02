# Stone_Paper_Scissor_Game

import random
import time

# Start of Game
print("Ready to play...")
time.sleep(2)
print("Let's see instructions :")
time.sleep(1)
print("1. Stone \n2. Paper \n3. Scissor \n") 

# Users choice
val = True
while(val):
    a = int(input("Enter Your Choice :"))
    if (a<1 or a>3):
        print("Wrong Choice ⚠")
    else:
        val = False
choice = {1:"Stone", 2:"Paper", 3:"Scissor"}
your_choice = choice[a]

print(f"Your choice = {your_choice}")

# Computer choice
b = random.randint(1,3)
computer_choice = choice[b]
time.sleep(1)
print(f"Computer choice = {computer_choice}")

# Finding winner of game
time.sleep(1)
print("\nFinding Conclusion....")
time.sleep(2)
if(computer_choice == your_choice):
    print("It's a Draw !")
else:
    if(a==1 and b==2):
        print("You lose !")
    elif(a==1 and b==3):
        print("You win !")
    elif(a==2 and b==1):
        print("You win !")
    elif(a==2 and b==3):
        print("You lose !")
    elif(a==3 and b==1):
        print("You lose !")
    elif(a==3 and b==2):
        print("You win !")
        