n=int(input("Enter the number of line that you want = "))
for i in range(n):
    a=65
    for j in range(i+1):
        print(chr(a),end=' ')
        a=a+1
    print()