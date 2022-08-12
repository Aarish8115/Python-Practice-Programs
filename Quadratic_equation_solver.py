from cmath import sqrt
import math
a=int(input("Enter x^2 coefficient\n"))
b=int(input("Enter x coefficient\n"))
c=int(input("Enter constant term\n"))
D=((b**2)-(4*a*c))
if D==0:
    print ("Roots are equal.")
    print((-b+(D**(1/2)))/2*a)
    print((-b-(D**(1/2)))/2*a)
elif D>0:
    print ("Roots are real and unequal.")
    print((-b+(sqrt(D)))/2*a)
    print((-b-(sqrt(D)))/2*a)
elif D<0:
    print("The roots are imaginary.")