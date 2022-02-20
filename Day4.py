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
hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# 0 rock - lose with 1, wins with 2
# 1 paper - lose with 2, wins with 0
# 2 scissors - lose with 0, wins with 1

if hand == 0:
  print(rock)

elif hand == 1:
  print(paper)

else:
  print(scissors)

print("computer choice:")
computer_hand = random.randint(0,2)

print(hand)
print(computer_hand)


if hand == 0 and computer_hand == 1:
  print(paper)

  print("You Lose")
  


elif hand == 0 and computer_hand == 2:
  print(scissors)

  print ("You Win")


elif hand == 1 and computer_hand == 0:
  print(rock)

  print("You Win")


elif hand == 1 and computer_hand == 2:
  print(scissors)

  print("You Lose")


elif hand == 2 and computer_hand == 0:
  print(rock)

  print("You Lose")


elif hand == 2 and computer_hand == 1:
  print(paper)

  print("You Win")

elif hand == computer_hand:
  print("it's a draw")
else:
  print("try again")

