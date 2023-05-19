import random
#create an input for the user to type their response

response = str(input("Would you like to play a game of rock, paper, or scissors? ")).capitalize()
response = str(response).strip()

#went ahead and accounted for variances by capitalizing 1st letter as well as replacing empty space
if response == "Yes":
    answer = input("Now decide... rock paper or scissors!? ")
elif response == "No":
    print("Bye scaredy cat")
else:
    print("Does not compute beep beep beep")

#create an answer for program to respond to the game
x = random.randint(1,3)
if x == 1:
    x = str("Rock")
elif x == 2:
    x = str("Paper")
else:
    x = str("Scissors")
print("Bot chooses", x)
#choose a winner
if x == "Rock":
    if answer == "Paper":
        print("You win!")
    elif answer == "Rock":
        print("You tie")
    else:
        print("You lose")
elif x == "Paper":
    if answer == "Scissors":
        print("You win!")
    elif answer == "Paper":
        print("You tie")
    else:
        print("You lose")
elif x == "Scissors":
    if answer == "Rock":
        print("You win!")
    elif answer == "Scissors":
        print("You tie")
    else:
        print("You lose")




