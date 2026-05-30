n=int(input("Enter the number = "))
a=0
temp=n
size=0
while n>0:
    size=size+1
    n=n//10
n=temp
while n>0:
    a=a+(n%10)**size
    n=n//10
if a==temp:
    print("This is the Armstrong Number.")
else:
    print("This is not the Armstrong Number.")