#to check if the given number is binary or not
# Return true if str is binary, else false
def isBinary(str):
    #code here
    for i in range(len(str)):
        if str[i] == "1" or str[i] == "0":
            continue
        else:
            return False
    return True
            
