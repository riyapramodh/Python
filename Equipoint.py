#fing the pt in array (1-indexed)suvh that the sum of elements to its left will be equal to the sum of elements to its right
    def equilibriumPoint(self,A, N):
        lsum = 0
        rsum = sum(A)
        for i in range(N):
            rsum -= A[i]
            
            if lsum == rsum:
                return i+1
            lsum += A[i]
