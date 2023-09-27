'''
QUES:
Perfect array= reverse of array matches the original array
'''

class Solution:
    def IsPerfect(self,arr,n):
        #Complete the function
        a=arr[::-1]
        if arr==a:
            return True
        return False
