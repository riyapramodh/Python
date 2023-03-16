#file function helps to read whats written inside a file
f = open("Riya.txt", "rt")
#r = f.read()
#print(r)
content1 = f.read(3)
print(content1)
content2 = f.read(2)
print(content2)
# content3 = f.read(10000) would print everything
f.close() #good to include the close function

for line in content1:#prints the line(words) in a content(one or so lines)
    print(line) #it prints charector by charector of each line of the txt file
# if you want to read the line not as in charector by charector but as an entire line then we need to majke the following changes:
file = open("Riya.txt")

#remove the f = file.read()
for line in file:#prints the line(line) in a file(many multiple lines)

print(file.readline()) #just reads one line at a time
#print(file.read()) reads all lines of the etxt file at a time
print(file.readlines())#prints a list of all lines
