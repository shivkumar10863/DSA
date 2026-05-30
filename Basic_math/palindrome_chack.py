n=int(input("Enter the number = "))
a=0
temp=n
while n>0:
    a=10*a+n%10
    n=n//10
if temp==a:
    print("This is the Palindrome Number.")
else:
    print("This is not the Palindrome Number.")
print("Entered number is ",temp," And the reverse number is ",a)