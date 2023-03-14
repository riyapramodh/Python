n = 49
print("guess the number game started")
print("guess what the number is?")
while True:
    a = int(input())
    if(a==n):
        print("YAY you've got it right")
        break
    else:
        print("OOPS you've got it wrong try again")
