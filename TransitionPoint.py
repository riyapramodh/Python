#find the point form which 1 will be present in a sorted array of 1s and 0s

#method1
def transitionPoint(arr, n):
    for i in range(n):
        if arr[i]==1:
            return i
    return -1
  
  #method2
  def transitionPoint(arr, n):
    for i in range(len(arr)):
        if arr[i] is 1:
            return i
    for i in arr:
        if i != 0:
            return 0
        if i != 1:
            return -1
 
