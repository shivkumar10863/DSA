n=int(input("Enter the number = "))
flag=True
for i in range(2,n//2+1):
    if n%i==0:
        flag=False
        break
if flag:
    print("This is the Prime Number.")
else:
    print("This is not the Prime Number.")