#to move all the zeros to the end and to leave the remaining unsorted array elements as it is

#method1

	def pushZerosToEnd(self,arr, n):
    	# code here
    	k = 0
 
    
        for i in arr:
            if i:
                arr[k] = i
                k = k + 1
 
    
        for i in range(k, len(arr)):
            arr[i] = 0
        
#method2

	A = [elem for elem in arr if elem == 0]
        arr = [elem for elem in arr if elem != 0]
        arr += A
   
#method3

    	A =[]
    	for i in range(n-1):
    	    if arr[n-1] == 0:
    	        h = arr.pop(n-1)
                A.append(h)
    	    if arr[i]==0:
    	        k = arr.pop(i)
    	        A.append(k)  
            arr = arr + A[:]   
#method4
    
        A = []
        B = []
        for i in range(n):
            if arr[i] == 0:
                A.append(arr[i])

        for j in range(len(A)):
            if A[j] == arr[j]:
                arr.pop(j)
        
        arr = arr + A[:]
        
