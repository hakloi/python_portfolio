import os
import random

# code begins
clear = lambda: os.system('cls')
clear()

# worst-case scenario
def quicksort(array):
    if len(array) < 2: #BASE CASE = [], [element] 
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot] #срез массива с 1 эл, т.е. начало [2]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
# best-case scenario
def quicksortbest(array):
    if len(array) < 2: #BASE CASE = [], [element] 
        return array
    else:
        mid = (0+len(array)-1)//2 
        pivot = array[mid]
        less = [i for i in array[1:] if i <= pivot] #срез массива с 1 эл, т.е. начало [2]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

array = []
n = 10
for i in range(n):
    array.append(random.randint(1,22))
print("Initial array: ")
print(array)

print("Sorted array with worst quicksort:")
print(quicksort(array))

print("Sorted array with best quicksort:")
print(quicksort(array))

