r=int(input("Enter the last limit of the number = "))
def num(n):
    if n==0:
        return 1
    print(n)
    num(n-1)
num(r)