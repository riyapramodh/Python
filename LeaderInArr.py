#to find the leader in the array
# in A = [16,17,4,3,5,2] we need to get ---> 17 5 2

def leaders(self, A, N):
       
        stack = [A[-1]]
        for i in range(N-2,-1,-1):
            if A[i]>=stack[-1]:
                stack.append(A[i])
        return stack[::-1]
