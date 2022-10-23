# 12. Write a python program to copy all the elements of one array into another array.

arr_1 = [1, 2, 3, 4, 5]
arr_2 = [None] * len(arr_1)

for i in range(0, len(arr_1)):
    arr_2[i] = arr_1[i]
    
print('Elements of original array: ')

for i in range(0, len(arr_1)):
    print(arr[i]),

print()

for i in range(0, len(arr_2)):
    print(arr_2[i])