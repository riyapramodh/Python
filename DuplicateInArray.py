#method 1
def duplicates(self, arr, n): 
    	# code here
    	arr.sort()
    	brr = []
    	crr = []
    	for i in range(0,n-1):
    	    if arr[i] == arr[i+1] and arr[i] in brr:
    	        continue;
    	    elif arr[i] == arr[i+1] and arr[i] not in brr:
    	        brr.append(arr[i])
    	   #     if arr[i] in brr:
    	   #         continue;
    	   #     else:
    	   #         brr.append(arr[i])
    	    else:
    	        continue;
    # 	if arr[n-2] == arr[n-1]:
    # 	    brr.append(arr[n-2])
        
    	if len(brr) == 0:
    	    return [-1]
        else:
            return brr
          
          
          
#method 2
def duplicates(self, arr, n): 
    	# code here
    	arr.sort()
    	brr = []
    	last = None
    	for i in range(0,n-1):
    	    if arr[i] == arr[i+1] and arr[i] != last:
    	        brr.append(arr[i])
    	        last = arr[i]
      if not brr:
    	    return [-1]
    	return sorted(brr)
