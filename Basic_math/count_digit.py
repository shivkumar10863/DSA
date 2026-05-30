n=int(input("Enter the number = "))
a=0
while n//10!=0:
    n=n//10
    a=a+1
print("Totel digit in this number is ",a+1)