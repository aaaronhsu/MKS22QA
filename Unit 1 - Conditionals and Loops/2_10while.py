import random

# classwork
def squareit(x):
    if x <= 8:
        print(x ** 2)
        squareit(x + 1)

def num():
    i = -1
    while i <= 5:
        i += 1
        if i == 3 or i == 6:
            continue
        print(i)

# homework
def guess():
    guess = int(input("Guess number: "))
    while(guess != random.randint(1, 9)):
        print("You guessed wrong")
        guess = int(input("Guess again: "))
    print("Your guess was correct")

# challenge
def password():
    p = input("Enter password: ")
    ln = len(p)
    lower = False
    upper = False
    special = False
    number = False

    if ln < 6 or ln > 16:
        print("bad password")
        return

    for c in p:
        if 97 <= ord(c) <= 122:
            lower = True
        if 65 <= ord(c) <= 90:
            upper = True
        if ord(c) == 35 or ord(c) == 36 or ord(c) == 64:
            special = True
        if 48 <= ord(c) <= 57:
            number = True

    if(lower and upper and special and number):
        print("valid password")
    else:
        print("bad password")
