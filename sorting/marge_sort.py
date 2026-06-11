import numpy as np
def m(l,r):
    n_arr=[]
    i=j=0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            n_arr.append(l[i])
            i=i+1
        else:
            n_arr.append(r[j])
            j=j+1
    n_arr.extend(l[i:])
    n_arr.extend(r[j:])
    return n_arr
def ms(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=ms(left)
    right=ms(right)
    return m(left,right)
n=int(input("Enter the length of the array = "))
arr=np.empty(n,dtype=int)
print("Enter the elements of the array => ")
for i in range(n):
    arr[i]=int(input(" "))
print("The sorted array is ",np.array(ms(arr)))