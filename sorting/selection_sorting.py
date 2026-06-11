import numpy as np
n=int(input("Enter the length of the array = "))
arr=np.empty(n,dtype=int)
print("Enter the element of the array => ")
for i in range(n):
    arr[i]=int(input(" "))
c=int(input("Press 1 for Ascending and 2 for Descending = "))
for i in range(n-1):
    if c==1:
        a=65000
    elif c==2:
        a=0
    else:
        print("You press wrong key only two option do you have 1 or 2 so restart it")
        exit()
    b=0
    for j in range(i,n):
        if c==1:
            if arr[j]<a:
                a=arr[j]
                b=j
        elif c==2:
            if arr[j]>a:
                a=arr[j]
                b=j
    arr[b]=arr[i]
    arr[i]=a
print("The sorted array is ",arr)