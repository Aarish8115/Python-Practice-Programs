import random

def playgame():
    result=""

    comp=random.randint(1,3)
    if comp==1:
        comp="rock"
    elif comp==2:
        comp="paper"
    elif comp==3:
        comp="scissor"

    print("Choose rock(r), paper(p) or scissor(s)")
    user=input("Your turn :")
    if (user=="r"):
        user="rock"
    elif (user=="p"):
        user="paper"
    elif(user=="s"):
        user="scissor"
    if comp=="rock":
        if user=="rock":
            result="It's a Tie"
        elif user=="scissor":
            result="You Lose..."
        elif user=="paper":
            result="You Won!"
    elif comp=="paper":
        if user=="paper":
            result="It's a Tie"
        elif user=="rock":
            result="You Lose..."
        elif user=="scissor":
            result="You Won!"
    elif comp=="scissor":
        if user=="scissor":
            result="It's a Tie"
        elif user=="rock":
            result="You Won!"
        elif user=="paper":
            result="You Lose..."
    print("Comp:",comp)
    print("You:",user)
    print(result)


playgame()