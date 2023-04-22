#for a giiven number of shift the user needs to rotate the array
#if A =[1,2,3,4,5] and D = 2 (d>len(A) also possible) --->  A = [3,4,5,1,2]

#method1
def rotateArr(self,A,D,N):
  for i in range(D):
            # remove_and_append(A, D)
            k = A.pop(0)
            A.append(k)
        return A
#mthod2
def rotateArr(self,A,D,N):
  if D>N:
            D = D%N
        A[:] = A[D:] + A[:D]
