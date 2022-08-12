mark=int(input("Enter your marks :"))

if (mark>100):
    print(None)
elif(mark>=90 and mark<=100):
    print("You got A grade!!")
elif(mark>=80):
    print("You got B grade.")
elif(mark>=70):
    print("You got C grade.")
elif(mark>=60):
    print("You got D grade.")
elif(mark>=50):
    print("You got E grade.")
else:
    print("You got F grade , you failed.")

