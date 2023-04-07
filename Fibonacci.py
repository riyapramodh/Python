def fibonacci_iterative(n):
    num = 0
    for i in range(n):
        num = i + num-1
    return num
n = int(input("enter the limit: "))
print(fibonacci_iterative(n))

def fibonacci_recursive(n1):
    if n1 == 1:
        return 0
    elif n1 == 2:
        return 1
    else:
        return fibonacci_recursive(n1-1) + fibonacci_recursive(n1-2)
n1 = int(input("enter the limit: "))
print(fibonacci_recursive(n1))
