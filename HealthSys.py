print("please enter yor name:")
name = str(input())
def time():
    import datetime
    return datetime.datetime.now()
if name =="Aia":
    f1 = open("aex.txt")
    time()
    print(f1.read())
    print("enter your weight:")
    x1 = int(input())
    f1.write("my weight is:")
    print(f1.read())
    f1.close()
elif name == "Bia":
    f2 = open("bex.txt")
    time()
    print(f2.read())
    f2.close()
elif name == "Cia":
    f3 = open("cex.txt")
    time()
    print(f3.read())
    f3.close()
#file - aex
i am Aia and i have cancer hence i should take chemotherapy regularly and eat well
#file - bex
ii am Cia and i have tuberculosis so i need to take medicines on time and eat well
#file - cex
My nam ei sCia and i am diabetic hence i should take insulin shots reguulary and go for the checkup more frequently than usual
