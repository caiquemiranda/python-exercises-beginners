# 16. Write a python program to print the elements of an array in reverse order.

arr = [1, 2, 3, 4, 5]

print('Original array : ')

for i in range(0, len(arr)):
    print(arr[i])

print('Array in reverse order: ')

reverse_arr = arr[::-1]

for i in range(0, len(reverse_arr)):
    print(reverse_arr[i])