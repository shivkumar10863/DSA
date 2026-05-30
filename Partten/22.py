n=int(input("Enter the number of line that you want = "))
for i in range(2*n-1):
    for j in range(2*n-1):
        t=i
        l=j
        r=2*n-2-j
        d=2*n-2-i
        a=n-min(min(t,l),min(r,d))
        print(a,end=' ')
    print()