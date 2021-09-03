'''  Add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, 
leave it unchanged'''

#my soution
def add_ing(str1):
    if len(str1) >= 3:
        if 'ing' in str1:
            print(str1 + 'ly')
        else:
            print(str1 + 'ing')
    else:
        print('No change needed')
add_ing('Hi')
add_ing("love")
add_ing('loveing')

#sample solution
def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))
