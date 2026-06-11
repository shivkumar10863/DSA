def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[x for x in arr[1:] if x<=pivot]
    right=[x for x in arr[1:] if x>pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
n=int(input("Enter the length of the array = "))
arr=[]
print("Enter the elements of the array => ")
for i in range(n):
    arr.append(int(input()))
print("The sorted array is ",quick_sort(arr))