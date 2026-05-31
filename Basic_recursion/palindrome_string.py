st=input("Enter the string = ")
n=len(st)
flag=True
s=0
e=n-1
for i in range(n//2):
    if st[s]==st[e]:
        flag=True
    else:
        flag=False
        break
    s=s+1
    e=e-1
if flag:
    print("This string is Palindrome.")
else:
    print("This string is not the Palindrome ")