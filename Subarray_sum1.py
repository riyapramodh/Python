#finds a subarray with an array of positive and negative number swhose trems add up to a sum of 0
class Solution:
    def maxLen(self, n, arr):
        #Code here
        hash_map = {}
 
        # Initialize result
        max_len = 0
 
        # Initialize sum of elements
        curr_sum = 0
 
        # Traverse through the given array
        for i in range(len(arr)):
 
            # Add the current element to the sum
            curr_sum += arr[i]
 
            if curr_sum == 0:
                max_len = i + 1
 
            # NOTE: 'in' operation in dictionary
            # to search key takes O(1). Look if
            # current sum is seen before
            if curr_sum in hash_map:
                max_len = max(max_len, i - hash_map[curr_sum])
            else:
 
                # else put this sum in dictionary
                hash_map[curr_sum] = i
 
        return max_len
