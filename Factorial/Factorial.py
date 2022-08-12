def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial
def trailingZeroes(n):
    count=0
    i=5
    while((n//i)!=0):
        count+=int(n/i)
        i=i*5
    return count
n=int(input("Enter Number :\n"))
# print(factorial(n))
print(trailingZeroes(n))