'''
Get a single string from two given strings, separated by a 
space and swap the first two characters of each string'''

def single (str1, str2):
    x = str1[2]
    str1 = str1.replace(str1[2], str2[2])
    str2 = str2.replace(str2[2], x)
    
    return str1 + ' ' + str2
print(single('lie','tru'))
