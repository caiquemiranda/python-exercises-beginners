# 14. Write a python program to find the smallest element in an array.

arr = [23, 11, 56, 23, 87]

min = arr[0]

for i in range(0, len(arr)):
    if(arr[i] < min):
        min = arr[i]
        
print(f'Smallest element present in given array: {str(min)}')
