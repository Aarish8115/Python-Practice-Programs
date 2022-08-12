import random

a=random.randint(1,20)

b=int(input("Guess the number between 1-20\n"))

while b!=a:
    if a>b:
        b=int(input("Enter  a larger number\n"))
    elif a<b:
        b=int(input("Enter a smaller number\n"))
if a==b :
    print("You guessed the right number.")
