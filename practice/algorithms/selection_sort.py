import os

# code begins
clear = lambda: os.system('cls')
clear()

def biggest_element(lst):
    biggest_value = lst[0]
    biggest_index = 0
    for i in range(1, len(lst)):
        if biggest_value < lst[i]:
            biggest_value = lst[i]
            biggest_index = i
    return biggest_index
        
def selection_sort_descending(lst):
    new_lst = []
    for i in range(len(lst)):
        biggest = biggest_element(lst)
        new_lst.append(lst.pop(biggest))
    return new_lst

lst = [1, 2, 3, 6, 9, 10, 23, 56, 12, 0, 8]
print('The biggest index is:')
print(biggest_element(lst))

print('\nResult descending list: ')
print(selection_sort_descending (lst))

# ------------------------------

def find_smallest(lst):
    smallest_value = lst[0]
    smallest_index = 0
    for i in range(1, len(lst)):
        if smallest_value > lst[i]:
            smallest_value = lst[i]
            smallest_index = i
    return smallest_index

def selection_sort_ascending(lst):
    new_lst = []
    for i in range(len(lst)):
        smallest = find_smallest(lst)
        new_lst.append(lst.pop(smallest))
    return new_lst

lst_second = [1, 2, 3, 6, 9, 10, 23, 56, 12, 0, 8]
print('\nThe smallest index is:')
print(find_smallest(lst_second))
print('\nResult ascending list:')
print(selection_sort_ascending(lst_second))

