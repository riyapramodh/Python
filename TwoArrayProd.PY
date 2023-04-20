#given two arrays we need to find the sum of the minimum product between their elements
#so here i have sorted one array in decending order and one array in the ascending order and multiplied their ith indices with each other followed by adding them up

class Solution:
    def minValue(self, a, b, n):
        # Your code goes here
        sum = 0
        #method 1 to sort array in descending order 
        
        #temp = 0
        # for x in range(0,len(a)):
        #     for y in range(x+1,len(a)):
        #         if a[x]<a[y]:
        #             temp = a[x]
        #             a[x] = a[y]
        #             a[y] = temp
        
        #method 2 to sort array in descending order
        a.sort(reverse=True)
        #sort array in ascending order
        b.sort()
        
                
        for i in range(n):
            s = a[i]*b[i]
            sum += s

        return sum
