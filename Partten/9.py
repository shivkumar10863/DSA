n=int(input("Enter the number of line that you want = "))
if n%2==0:
    n1=n//2
    for i in range(0,n1):
        for j in range(n1-i-1,0,-1):
            print(end=' ')
        for k in range(2*i+1):
            print('*',end='')
        print()
    for i in range(n1-1,-1,-1):
        for j in range(n1-i-1,0,-1):
            print(end=' ')
        for k in range(2*i+1):
            print('*',end='')
        print()
else:
    n1=n//2
    for i in range(0,n1+1):
        for j in range(n1-i,0,-1):
            print(end=' ')
        for k in range(2*i+1):
            print('*',end='')
        print()
    for i in range(n1-1,-1,-1):
        for j in range(n1-i,0,-1):
            print(end=' ')
        for k in range(2*i+1):
            print('*',end='')
        print()