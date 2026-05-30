n=int(input("Enter the number of line that you want = "))
if n%2==0:
    n1=n//2
    for i in range(1,n1+1):
        for j in range(i):
            print('*',end='')
        print()
    for i in range(n1,0,-1):
        for j in range(i):
            print('*',end='')
        print()
else:
    n1=n//2
    for i in range(1,n1+2):
        for j in range(i):
            print('*',end='')
        print()
    for i in range(n1,0,-1):
        for j in range(i):
            print('*',end='')
        print()