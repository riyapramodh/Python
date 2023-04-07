a = 49 #global variable
c = 100
def riya(n):
    a = 50 #local variable
    b = 30
    print(n,"this is pramod")
    print(a,b)
    #we can perform ++ and -- on local variables within a function
    #if we wantto perform the same on a global variable then we need to use the keyword "global"
    global c
    c = c+2
    b = b+1
    print(c,"--> changed the global variable yay")
    print(b)
riya("hi riya")
print(a)
#here "a" is a global variable hence its just a read only function and inside the function we cannot perform increment or decrement "a"
a = a-1
print(a)
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#nested function
def pramod():
    x = 50
    def vvns():
        global x
        x = 49
    print("befor calling vvns() = ",x)
    vvns()
    print("after calling vvns() = ",x)#they wont read the modified value as they would go out to chehck for x since its mentioned global and not for a nested function its outer nest is considred to be global
pramod()
print(x)#now it looks within the function hence would print 49
