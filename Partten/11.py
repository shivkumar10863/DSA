n=int(input("Enter the number of line that you want = "))
a=1
for i in range(n):
    for j in range(i+1):
        print(a,end=' ')
        if a==0:
            a=1
        else:
            a=0
    print()