# 17. Write a python program to sort the elements of an array in ascending order.

arr = [5, 2, 8, 7, 1]

temp = 0

print('Elemnts of original array: ')
for i in range(0, len(arr)):
    print(arr[i])
    
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if (arr[i] > arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            
print()

print('Elements of array sorted in ascending order: ')
for i in range(0, len(arr)):
    print(arr[i], end=' ')