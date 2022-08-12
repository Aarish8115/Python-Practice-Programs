from datetime import datetime


recieptno=0
total = 0
now=datetime.now()
date_=now.strftime("%d/%m/%Y %H:%M:%S")
start=input("To start calculator press \"s\"\n")
while (start=="s"):
    #recieptno=input("Enter reciept no.\n")
    name=input("Enter recipient name \n")
    recieptno=recieptno+1
    while (True):
        price=input("Enter item price or press q to quit\n")
        if (price!="q"):
            total=total+int(price)
            print(f"Your total so far {total}")
        else:
            with open(f"reciepts/{recieptno}.txt","w") as i:
                i.write(f"Reciept No. {recieptno}\nName {name}\nTotal Rs.{total}\n{date_}")
            print(f"Your total is {total}.\nThankyou for shopping with us.")
            break
    start = input("Enter s to start again\nq")

