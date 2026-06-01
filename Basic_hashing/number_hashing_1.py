''' In this the limt of thr biggest number in the input array is 10 to the power 6 greater 
then this value is not except by the programm'''
import numpy as np
n=int(input("Enter the length of the array = "))
arr=np.empty(n)
print("Enter the element of the array => ")
for i in range(n):
    arr[i]=int(input(" "))
a=0
for i in range(n-1):
    if arr[i]>a:
        a=arr[i]
hsar=np.zeros(int(a+1),dtype=int)
for i in range(n):
        hsar[int(arr[i])]=hsar[int(arr[i])]+1
while True:
    a=input("Enter the number for get the frequency for exit press N(n) = ")
    if a=='n' or a=='N':
        break
    print("The frequency of this number is ",hsar[int(a)])