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
a=(rock)
b=(paper)
c=(scissors)
game=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if game == 0:
  print(f"{a}")
elif game == 1:
  print(f"{b}")
elif game == 2:
  print(f"{c}")
elif game >2:
  print("invalid number")

print("computer chose")

import random
final=random.randint(0, 2)
if final==0:
  print(f"{a}")
elif final==1:
  print(f"{b}")
elif final==2:
  print(f"{c}")

if game==0 and final==0:
  print("draw")
elif game==0 and final==1:
  print("you lose")
elif game==0 and final==2:
  print ("you win")

elif game==1 and final==0:
  print("you win")
elif game ==1 and final==1:
  print("draw match")
elif game ==1 and final ==2:
  print("you lose")

elif game==2 and final==0:
  print("you lose")
elif game==2 and final==1:
  print("you win")
elif game==2 and final==2:
  print("draw match")