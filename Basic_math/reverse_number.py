n=int(input("Enter the number = "))
a=0
while n>0:
    a=10*a+n%10
    n=n//10
print("So the reverse number is ",a)