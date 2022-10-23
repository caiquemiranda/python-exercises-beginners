# 15. Write a python program to print the sum of all elements in an array.

arr = [1, 2, 3, 4, 5]

sum = 0

for i in range(0, len(arr)):
    sum = sum + arr[i]

print(f'Sum of all the elments of an array: {str(sum)}')