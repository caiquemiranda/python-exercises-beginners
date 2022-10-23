# 8. Write a python program to find lcm

def calculate_lcm(x, y):
    if x > y:
        greater = x
    
    else:
        greater = y
        
    while(True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    
    return lcm

num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))

print(f'The L.C.M. of {num_1} and {num_2} is {calculate_lcm(num_1, num_2)}')