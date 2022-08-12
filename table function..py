def table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}",)
    return ""


a=int(input())
print(table(a))