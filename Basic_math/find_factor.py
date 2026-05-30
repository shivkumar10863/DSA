n=int(input("Enter the number = "))
a=[]
for i in range(1,n//2+1):
    if n%i==0:
        a.append(i)
a.append(n)
print("All factors of your entered number is ",a) 