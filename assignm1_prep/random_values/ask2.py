import random

random_num = random.randint(1, 100)
print(random_num)

found = False

while found == False:
    num = int(input("Guess the number: "))
    if int(num) == random_num:
        found = True
        print("You found the number! Congrats!")
    else:
        if num < random_num:
            print("Wrong number. Guess higher!")
        else:
            print("Wrong number. Guess lower!")
