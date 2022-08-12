a=int(input("Enter side 1\n"))
b=int(input("Enter side 2\n"))
c=int(input("Enter side 3\n"))

s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**(1/2)
print(area)