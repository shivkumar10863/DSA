n=int(input("Enter the number of line that you want = "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()