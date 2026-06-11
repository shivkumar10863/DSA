import numpy as np 
n=int(input("Enter the length of the array = "))
arr=np.empty(n,dtype=int)
print("Enter the elements of the array => ")
for i in range(n):
    arr[i]=int(input(" "))
c=int(input("Press 1 for Ascending and 2 for Descending = "))
for i in range(n-1):
    for j in range(n-i-1):
        if c==1:
            if arr[j]>arr[j+1]:
                arr[j]=arr[j]+arr[j+1]
                arr[j+1]=arr[j]-arr[j+1]
                arr[j]=arr[j]-arr[j+1]
        elif c==2:
            if arr[j]<arr[j+1]:
                arr[j]=arr[j]+arr[j+1]
                arr[j+1]=arr[j]-arr[j+1]
                arr[j]=arr[j]-arr[j+1]
        else:
            print("You press wrong key only two option do you have 1 or 2 so restart it")
            exit()
print("The sorted array is ",arr)