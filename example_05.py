def numberCheck(s):
    if s > 0:
        print('Number given by you is Positive.')
    
    elif s < 0:
        print('Number given by you is Negative.')
    
    else:
        print('Number given by you is zero')
        
s = float(input("Enter a number as input value: "))
numberCheck(s)