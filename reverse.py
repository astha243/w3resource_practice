'''Write a Python program to reverse a string.'''
def reversing (str1):
    if len(str1) * 1 == 4: 
        print(str1[len(str1)::-1])
    else:
        print('Doesn\'t match ' )
    
reversing('hell')
reversing('what??')
