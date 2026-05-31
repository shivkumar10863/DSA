n=int(input("Enter how many time do you want to print the name = "))
name=input("Enter your that you want to print = ")
def nam(n):
    if n==0:
        return 1
    print(name)
    nam(n-1)
nam(n)