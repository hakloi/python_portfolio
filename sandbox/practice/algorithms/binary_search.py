import os

# code begins
clear = lambda: os.system('cls')
clear()

def binary_search(lst, item):
    low = 0 
    high = len(lst) - 1 
    while low <= high: 
        mid_index = (low + high)//2
        mid_value = lst[mid_index]
        if mid_value == item:
            return mid_index
        elif mid_value > item: 
            high = mid_index - 1
        else: 
            low = mid_index + 1
    return None

lst = list(range(1, 15))
print("List: ", lst)  
  
if binary_search(lst, 2) is not None:
    print("\nThe number 2",)
    print("Is found at index", binary_search(lst, 2))
else:
    print("Not found")