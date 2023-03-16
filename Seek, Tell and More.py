f = open("Riya.txt")
print(f.tell())#tells you where is your file pointer located
print(f.readline())
f.seek(0) #it will seek back its index or jump back to the position mentioned and starts printin from that index on ward:1 means first index onwars and so on
print(f.readline())
f.seek(10)#tells you that the file pointer is at 10 and hence it would start from the 10th index
print(f.tell())#same expl as above line so its value would be dispayed as 10(wtv index position itstarts from
print(f.readlines())
f.close()
