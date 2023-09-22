print("TIME COMPLEXITY")
'''
WHAT IS TIME COMPLEXITY?
-Time complexity is defined as the amount of time taken by an algorithm to run, as a function of the length of the input. 
-It measures the time taken to execute each statement of code in an algorithm.

- The Time Complexity of an algorithm/code is not equal to the actual time required to execute a particular code,
but the number of times a statement executes. We can prove this by using the time command. 

- The O -> is called Big – Oh which is an asymptotic notation.
- EXAMPLES:
'''
print("Hello World") # O(n)- printed only once
# -------------------
n = 8
for i in range(1, n + 1):
    print("Hello World !!!")  # O(N)-  printed only n times
#----------------------

n = 8
i = 2
for j in range(2,n+1):
    if(i >= n):
        break
    print("Hello World !!!")  
    i *= i                       #O(log(log n))
#----------------------------
a = 0
b = 0
for i in range(N):
  a = a + random()
 
for i in range(M):
  b= b + random()                # TC=O(M+N), S.C.=o(1)

#---------------------------
a = 0;
for i in range(N):
  for j in reversed(range(i,N)):
    a = a + i + j;            #TC= o(N*N)

'''
EXPLANATION- = N + (N – 1) + (N – 2) + … 1 + 0 
= N * (N + 1) / 2 
= 1/2 * N^2 + 1/2 * N 
O(N^2) times. '''
#--------------------------------------
k = 0;
for i in range(n//2,n):
  for j in range(2,n,pow(2,j)):
        k = k + n / 2;                  #TC= o(n*logn)
'''
EXPLANATION =  j keeps doubling till it is less than or equal to n. Several times, we can double a number till it is less than n would be log(n). 
Let’s take the examples here. 
for n = 16, j = 2, 4, 8, 16 
for n = 32, j = 2, 4, 8, 16, 32 
So, j would run for O(log n) steps. 
i run for n/2 steps. 
So, total steps = O(n/ 2 * log (n)) = O(n*logn)'''



