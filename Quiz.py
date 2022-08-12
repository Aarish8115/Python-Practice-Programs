def play_game():
    q1="What is the full form of CPU?"
    a1="central processing unit"
    q2="What is the latest version of windows?"
    a2="windows 11"
    q3="How many days do we have in a week?"
    a3="7"
    q4="How many colours are there in a rainbow?"
    a4="7"
    q5="How many letters are there in the english alphabet?"
    a5="26"
    m=0
    print(q1)
    u1=input("Answer : ")
    if u1==a1:
        print("Correct!")
        m+=1
    else:
        print("Wrong.")
    print(q2)
    u2=input("Answer : ")
    if u2==a2:
        print("Correct!")
        m+=1
    else:
        print("Wrong.")
    print(q3)
    u3=input("Answer : ")
    if u3==a3:
        print("Correct!")
        m+=1
    else:
        print("Wrong.")
    print(q4)
    u4=input("Answer : ")
    if u4==a4:
        print("Correct!")
        m+=1
    else:
        print("Wrong.")
    print(q5)
    u5=input("Answer : ")
    if u5==a5:
        print("Correct!")
        m+=1
    else:
        print("Wrong.")

    print(f"You score {m}/5")


print("Welcome to the Quizz!\nAnswer these simple questions to test you GK:\n")
a=input("Do you wnat to play\nYes(y) or No(n)\n")
if a=="y":
    play_game()
else:
    print("OK")