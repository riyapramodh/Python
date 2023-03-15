#exception handling
def practise():
    """useful for printing error messages while connecting to the internet. if the connection is lost/is not possible due to network connectivity problem then we can ensure that the code still works all fine by using this method"""

    print("enter the first number:")
    a = input()
    print("enter the second number:")
    b = input()
    try:
        print("the sum of a and b is :", int(a) + int(b))
    except Exception as e:
        print(e)
    print("_______________________________________________________________________________________________________")
    print("the processing and running of the code has been done and it is capable to catch the error(if any)")
    print("________________________________________________________________________________________________________")

print(practise().__doc__)
