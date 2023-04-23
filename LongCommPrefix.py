#arr[] = {geeksforgeeks, geeks, geek,geezer} ---> "gee" is the longest common prefix in all the given strings.
    def longestCommonPrefix(self, arr, n):
        # code here
        prefix = arr[0]
        if not arr:
            return -1
        for s in arr[1:]:
            i = 0
            while i<len(s) and i< len(prefix) and prefix[i] == s[i]:
                i +=1
            prefix = prefix[:i]
        if not prefix:
            return -1
        return prefix
      
      
      
      
      
      
#longer method
#code for seperating charectors from a string
charS = []
for string in arr:
  for char in string:
    charS.append(char)
return charS

#code for chehcking the number of times the charector has appeared in the array
charNum = []
for char in charS:
  if char not in charNum:
    charNum[char] = 1
   else:
    charNum[char] += 1
 
#code for chehcking the number of times the charector has appeared in the strings present in the array
charCmn = []
for char, count in charNum.items():
    if count == len(arr):
        charCmn.append(char)
#code for finding common prefix of all stringd
prefix = ''
if charCmn:
    for i, char in enumerate(arr[0]):
        if char not in charCmn:
            break
        prefix += char
    print(f"The common prefix is: {prefix}")
    print(f"There are {len(common_chars)} common characters in all strings")
else:
    print("There are no common characters in all strings")





