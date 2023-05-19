import random
name = input("What is your name? ")
question = input("What is your question? ")
answer = ""
print(name + " asks: " + question)
print("Magic 8-Ball's answer:")
rn = random.randint(1,9)
# rn = random number
if rn == 1:
 print("Yeah for sure")
elif rn == 2:
  print("I don't think so buddy")
elif rn == 3:
  print("No way Jose")
elif rn == 4:
  print("In your dreams!")
elif rn == 5:
  print("I dont recommend, but yes")
elif rn == 6:
  print("Without a doubt yes")
elif rn == 7:
  print ("Never in a million years")
elif rn == 8:
  print ("No silly goose")
elif rn == 9:
  print ("No zont zoo it")
else:
  answer = "Error"

