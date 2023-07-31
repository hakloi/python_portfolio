import os
import random

# code begins
clear = lambda: os.system('cls')
clear()

def binary_search(lst, item):
    low = 0 
    high = len(lst) - 1 
    print(low, high)
    
    while low <= high: 
        mid = (low + high)//2
        print(mid)
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item: 
            high = mid - 1
        else: 
            low = mid + 1
            return None

lst = list(range(1, 15))
print("List: ", lst)  
  
if binary_search(lst, 2) is not None:
    print("Found at index", binary_search(lst, 2))
else:
    print("Not found")