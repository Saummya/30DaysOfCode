'''
QUES:



'''
class Solution:
    def longest(self, names, n):
    	# code here
    	l=0
    	for i in names:
    	    k=len(i)
    	    if k>l:
    	        maxstr=i
    	        l=k
    	        
    	return maxstr
    	    
    	
    	
