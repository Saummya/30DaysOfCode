'''
QUESTION:
An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
Given an array arr[] of size N, Return the index of any one of its peak elements.
Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0. 


Example 1:

Input: 
N = 3
arr[] = {1,2,3}
Possible Answer: 2
Generated Output: 1
Explanation: index 2 is 3.
It is the peak element as it is 
greater than its neighbour 2.
If 2 is returned then the generated output will be 1 else 0.
Example 2:

Input:
N = 3
arr[] = {3,4,2}
Possible Answer: 1
Output: 1
Explanation: 4 (at index 1) is the 
peak element as it is greater than 
it's neighbor elements 3 and 2.
If 1 is returned then the generated output will be 1 else 0.
'''
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        for i in range(0,n):
            if (i==0 and arr[i]>arr[i+1]):
                return 0
                
            elif (i==n-1 and arr[i]>arr[i-1]):
                return n-1
            
            elif (i!=0 and arr[i]>arr[i-1] and arr[i]>arr[i+1]):
                return i
            
                
       
