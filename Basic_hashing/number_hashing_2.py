''' In this we not have any limit on the value of the input array '''
import numpy as np
n=int(input("Enter the length of the array = "))
arr=np.empty(n)
print("Enter the element of the array => ")
for i in range(n):
    arr[i]=int(input(" "))
hsar={}
for i in range(n):
        if arr[i] not in hsar.keys():
            hsar[int(arr[i])]=1
        else:
            hsar[int(arr[i])]=hsar[int(arr[i])]+1
while True:
    a=input("Enter the number for get the frequency for exit press N(n) = ")
    if a=='n' or a=='N':
        break
    if int(a) not in hsar.keys():
        print("The frequency of this number is 0")
    else:     
        print("The frequency of this number is ",hsar[int(a)])