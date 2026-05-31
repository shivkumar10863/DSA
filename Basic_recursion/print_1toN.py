r=int(input("Enter the last limit of the number = "))
b=1
def num(b,r):
    if b==r:
        print(b)
        return 1
    print(b)
    num(b+1,r)
num(b,r)