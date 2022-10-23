# 3. Write a python program to swap two variables without using a third variable.

P = int(input('Please enter value for P: '))
Q = int(input('Please enter value for Q: '))

P, Q = Q, P

print(f'The value of P after swapping: {P}')
print(f'The value of Q after swapping: {Q}')