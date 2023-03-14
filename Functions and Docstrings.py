def girl():
    print("i am a beautiful girl")
    print("my age is 21")
    print('my favourite colour is pink')
def boy(a,b):
    print("i am a handsome boy")
    print("i am 20 years old")
    print("my favourite colour is blue")
    print("sum of my age and height is", a+b)

girl()
boy(20,179)
#functions have docstring
def baby():
    print("this is a small baby and its age doesnt matter because its too cute")
    """these classes mainly discuss about the differenet gender and diff types of humans. this function depicts the babies hwo are the starting form of human life"""


print(baby().__doc__) # a comment that can be printed is a docstring and it can contain warnings, limits, etc
