n=int(input("Enter the number of line that you want = "))
a=65
for i in range(n):
    for j in range(i+1):
        print(chr(a),end=' ')
    a=a+1
    print()