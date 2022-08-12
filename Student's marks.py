# s1=input("First student name :")
# s2=input("Second student name :")
# s3=input("Third student name :")
# s4=input("Fourth student name :")
# s5=input("Fifth student name :")
# s6=input("Sixth student name :")

# m1=int(input("First student marks :"))
# m2=int(input("Second student marks :"))
# m3=int(input("Third student marks :"))
# m4=int(input("Fourth student marks :"))
# m5=int(input("Fifth student marks :"))
# m6=int(input("Sixth student marks :"))
# l1=[s1,s2,s3,s4,s5,s6]
# l2=[m1,m2,m3,m4,m5,m6]
# print('The marks of',l1,"are",l2,'respectively.')


n = int(input('Enter number of students '))
marks = []
name = []
for i in range(n): 
    a=input("Enter name ")
    name.append(str(a))
    b=input(f"Enter marks of {a} ")
    marks.append(int(b))

for i in range(n):
    print(name[i],":", marks[i])