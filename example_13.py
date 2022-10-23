# 13. Write a python program to find the largest element in an array.

arr = [23, 11, 56, 23, 87]

max = arr[0]

for i in range(0, len(arr)):
    if(arr[i] > max):
        max = arr[i]
        
print(f'Largest element present in given array: {str(max)}')
