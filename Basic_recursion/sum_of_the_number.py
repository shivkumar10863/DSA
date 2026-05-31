r=int(input("Enter the number = "))
def snum(n):
    if n==1:
        return 1
    return n+snum(n-1)
print("The sum of the number is ",snum(r))