# client_size = int(input())
# shoe_sizes = sorted(map(int, input().split()))

# count = 0 
# last_size = client_size - 3 

# for size in shoe_sizes:
#     if size >= client_size and size >= last_size + 3:
#         count += 1  
#         last_size = size 

# print(count)

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                lst[k] = left[i] 
                i+=1
            else: 
                lst[k] = right[j] 
                j+=1
            k+=1
        while i < len(left): 
            lst[k] = left[i] 
            i+=1
            k+=1
        while j < len(right): 
            lst[k] = right[j] 
            j+=1
            k+=1
    
    
lst = list(map(int, input().split()))
print(len(lst))
merge_sort(lst)
print(*lst)

# 5 2 3 6 84 9 8