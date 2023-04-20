#to find a subarray within an array whose sum will be equal to a user given input and to find the starting and ending index of that particular subarray
i,j = 0,0
        sum = 0
        while i<n:
            sum += arr[j]
            if sum >s and i<j:
                sum -+ arr[i]
                if sum == s:
                    return [i+1, j+1]
            if sum == s:
                return [i+1, j+1]
        return -1
