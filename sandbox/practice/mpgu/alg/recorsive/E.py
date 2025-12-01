def sum_seq(lst):
    if lst == []:
        return 0
    else:
        return lst.pop(0) + sum_seq(lst)

lst = []
while (w := int(input())) != 0:
    lst.append(w)
    
print(sum_seq(lst))

# Примеры
# входные данные
# 1
# 7
# 9
# 0
# выходные данные
# 17