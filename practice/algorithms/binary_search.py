import random

# 1st rule: list is in SORTED order 
def rand_list(n):
    lst = []
    for i in range(n):
        lst.append(random.randint(0,90))
    lst.sort()
    print(lst)

list = rand_list(10)
low = 0
high = list - 1