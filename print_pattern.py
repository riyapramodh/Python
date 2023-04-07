print("printing pattern")
num = int(input("enter 0 or 1: "))
n = int(input("enter the range: "))
if num ==0:
    for i in range(0,n + 1):
        print("*"*i)
elif num == 1:
    for i in range(n,-1,-1):
        print("*"*i)

