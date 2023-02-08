print("welcome to the faulty calculator and beware of the tricks!")
print("enter the first number:")
n1 = int(input())
print("please enter the second number:")
n2 = int(input())
print("please mention the choice of operation:")
op = str(input())
if op == "add":
    if n1==56 and n2 == 9:
        print("77")
    else:
        print(n1+n2)
elif op == "subtract":
    print(n1 - n2)
elif op == "multiply":
    if n1 == 45 and n2 == 3:
        print("555")
    else:
        print(n1*n2)
elif op == "divide":
    if n1 == 56 and n2 == 6:
        print("4")
    else:
        print(n1/n2)
else:
    print("wrong choice of operation please try again!")