import os
# code begins
clear = lambda: os.system('cls')
clear()

def insertion_sort(arr):
    for i in range (1, len(arr)):
        current_el = arr[i]
        j= i -1 #j = 0
        while j>=0 and current_el < arr[j]: #2 < 5
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] =  current_el
            
arr = [5,2,4,6,1,3]
print(arr)
insertion_sort(arr)
print(arr)