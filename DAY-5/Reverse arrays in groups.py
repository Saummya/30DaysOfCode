class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
		# code here
		for i in range(0,N,K):
            start=i
            end=min(i+K-1,N-1)
            
            while(start<=end):
                t=arr[start]
                arr[start]=arr[end]
                arr[end]=t
                
                start+=1
                end-=1
        return arr

'''
ques link: https://practice.geeksforgeeks.org/problems/reverse-array-in-groups0255/1?page=1&difficulty[]=-1&category[]=Arrays&sortBy=submissions
'''
