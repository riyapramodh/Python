def factorial_iterative(n):
    """

    :param n: Integer
    :return: n*(n-1)!
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

number1 = int(input("enter the number: "))
print("factorial using iterartive method",factorial_iterative(number1))



def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

number2 = int(input("enter the number: "))
print("factorial using recursive method",factorial_recursive(number2))
