def roundup(lst1):
    total = 0
    for num in lst1:
        total = sum(lst1)
        total = round(total) * len(lst1)
    return total
lst1=[1.5,2.4,3.5]
print(roundup(lst1))

        
