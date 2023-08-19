class Solution:
    def modify(self, s):
        # code here
        s = s.split() #splits all the words/chars without any whitespaces
        c = ""
        for i in s:
            c+=i
        return c
