num=int(input("Enter your number :"))
prime=True

for i in range(2,num//2):
    if (num%i==0):
        prime=False
        break
if prime:
    print("This is a prime number.")
else:
    print("This is a composite number.")