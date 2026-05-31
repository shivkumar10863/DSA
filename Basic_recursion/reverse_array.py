import numpy as np
r=int(input("Enter the length  of array = "))
print("Enter the elements of the array => ")
arr=np.empty(r)
for i in range(r):
    arr[i]=int(input("=> "))
print("The orignal array is ",arr)
def rarr(ar,n,s,e):
    if s==n//2 :
        return ar
    ar[s]=ar[s]+ar[e]
    ar[e]=ar[s]-ar[e]
    ar[s]=ar[s]-ar[e]
    return rarr(ar,n,s+1,e-1)
print("The reverse array is ",rarr(arr,r,0,-1))