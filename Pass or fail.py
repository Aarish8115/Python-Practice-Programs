sub1=int(input("Enter english marks :"))
sub2=int(input("Enter hindi marks :"))
sub3=int(input("Enter science marks :"))
avg=(sub1+sub2+sub3)/3

if (sub1<33 or sub2<33 or sub3<33 or avg<40):
    print("Sorry, you are Fail.")
else:
    print("Congratulations, you passed.")