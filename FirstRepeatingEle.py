#to find the first repeating elements and in case of them being more than 1 in number, return the ones with the least index

#code1 - main method code
        x=len(set(arr))
        if x==n:
            return '-1'
        else:
            for i in arr:
                if arr.count(i)>1:
                    return (arr.index(i)+1)

#code 2 = has time complexity 
    def firstRepeated(self,arr, n):
        
        #arr : given array
        #n : size of the array
        if len(arr) == 1:
            return -1
        for i in range(n):
            j = i+1
            while j<n:
                if arr[i] == arr[j]:
                    return i+1
                else:
                    j += 1
        return -1
      
#code 3
        if len(arr) == 1:
            return -1
        element_index_dict = {}
    
        for i in range(n):
            if arr[i] in element_index_dict:
                element_index_dict[arr[i]] +1
            else:
                element_index_dict[arr[i]] = i
            
        return -1
      
      
