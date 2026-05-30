n1=int(input("Enter the first number = "))
n2=int(input("Enter the second number = "))
n=max(n1,n2)
gcd=0
for i in range(1,n//2+1):
    if n1%i==0 and n2%i==0:
        gcd=i
print("Totel digit in this number is ",gcd)