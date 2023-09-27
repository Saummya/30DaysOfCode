#User function Template for python3

def getMinMax( a, n):
    max1=a[0]
    for i in range(1,n):
        if a[i]>max1:
            max1=a[i]
        
    min1=a[0]
    for i in range(1,n):
        if a[i]<min1:
            min1=a[i]
    
    return [min1, max1]
    
    
