n=int(input("Enter the number how many term you want to print = "))
a=0
b=1
def fib(n,a,b):
    if n<=2:
        return 1
    print(a+b,end=' ')
    b=a+b
    a=b-a
    return fib(n-1)
print("The Fibonacci series is ",a,b,end=' ')
fib(n,a,b)