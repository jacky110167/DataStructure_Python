import random

def QuickSort(lst):
    '''If the element of the list is smaller than key, put it before key'''
    '''If the element of the list is bigger than key, put it after key'''
    if len(lst) <= 1:
        return lst
    
    key = lst[0]
    
    smaller = [ i for i in lst if i < key]
    bigger  = [ i for i in lst if i > key]
    
    smaller = QuickSort(smaller)
    bigger = QuickSort(bigger)
    
    return smaller + [key] + bigger

lst = [i for i in range(1, 11)]
random.shuffle(lst)

print(lst)
print(QuickSort(lst))