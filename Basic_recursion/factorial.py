r=int(input("Enter the number for factorial = "))
def fac(n):
    if n==1 or n==0:
        return 1
    return n*fac(n-1)
print("The factorial of the number is ",fac(r))