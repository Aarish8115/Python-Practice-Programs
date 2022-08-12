def max(a,b,c,d):
    if a>b and a>c and a>d:
        return a
    elif b>c and b>d:
       return b
    elif c>d:
        return c
    else:
        return d

num1=int(input("Enter number 1 :"))
num2=int(input("Enter number 2 :"))
num3=int(input("Enter number 3 :"))
num4=int(input("Enter number 4 :"))
print(f"The greatest among {num1} , {num2} , {num3} , {num4} is {max(num1,num2,num3,num4)}")