import random
print("A dice is rolled...")
result = random.randint(1,6)
if result == 1:
    print("The result is 1!")
elif result == 2:
    print("The result is 2!")
elif result == 3:
    print("The result is 3!")
elif result == 4:
    print("The result is 4!")
elif result == 5:
    print("The result is 5!")
elif result == 6:
    print("The result is 6!")
else:
    print("Error try again")
if result <= 3 :
    print("Ooof not the best")
if result >= 4:
    print("You're pretty lucky")