'''Just trying to make a hand cricket game with the computer '''
import random
print("Welcome to Hand Cricket Game!🏏")
print('The rule of the hand cricket game is that you add the number that you have guessed to your score until and unless your score matches with the computer.\nIf your guess is matched with the computer then you are OUT!☝️')
print('Your turn')
a= random.randint(1,6)
b = int(input("Enter a number from 1 to 6:"))
score = 0
computer_score = 0
while a!=b:
    print(f"The computer choice is {a}")
    score += b
    a= random.randint(1,6)
    b = int(input("Enter a number from 1 to 6:"))
print("You are OUT!☝️")
print(f"Your score is {score}")
print("Now it's computer turn to play")
d = int(input("Enter a number from 1 to 6:"))
c= random.randint(1,6)
while c!=d:
    #print("Your choice is {d}")
    print(f"The computer choice is {c}")
    computer_score += c
    d = int(input("Enter a number from 1 to 6:"))
    c= random.randint(1,6)
print("Computer is OUT!☝️")
print(f"Computer score is {computer_score}")
if score > computer_score:
    print("You won the game!🥳")
elif score < computer_score:
    print("Computer won the game!😢")
else:
    print("It's a tie!🤝")
