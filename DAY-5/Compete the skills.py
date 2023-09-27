#User function Template for python3

class Solution:
    def scores(self, a, b, cc):
        # Update list cc of length 2 with cc[0] = ca and cc[1] = cb
        # Your code goes here
     
        for i in range(len(a)):
            if a[i]>b[i]:
                cc[0]+=1
            elif a[i]<b[i]:
                cc[1]+=1
            
          
        return cc
        
