def calculate_hcf(x, y):
    if x > y:
        smaller = y
    
    else:
        smaller = x
    
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
        
    return hcf

num_1 = int(input('Enter fisrt number: '))
num_2 = int(input('Enter second number: '))

print(f'The H.C.F of {num_1} and {num_2} is {calculate_hcf(num_1, num_2)}')