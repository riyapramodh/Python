f = open("Riya.txt","w") #denotes that we want to write to the file#write mode tells that nmw the contents of the file be new values will be replacing the old values
#by doing so it creates anew file and writes the following, else it replcaes the already written content with the newly written content in a preesixting file
f.write("Riya is deeply disturbed, watched upon and copied by a wicked girl\n")#the more you run it the more number of times it will be appended
#if we want toknow the NUMBER of charectors that we are typing onto the file then we can do as follows
a = f.write("however karma is a bigger bitch than she is\n")
print(a)
f.close()

"""
f = open("Riya.txt")
conetnet = f.read()
print(conetnet)
f.close()


f = open("riya.txt")
f.write("riya is a good girl")
f.close()
"""

g = open("Riya.txt","a")#append mode   says that the newer values will just be appended onto the end of the file
g.write("pramod hates that dumb girl too\n ")
g.close()


#to handle both the read and write
k = open("Riya.txt","r+") #helps you to both, read and write
k1 = k.read()
print(k1)
k2 = k.write("Bye Bye")
print(k2)
k.close()
