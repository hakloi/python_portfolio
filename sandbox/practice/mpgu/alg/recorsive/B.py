def sum(a, b):
    if b == 0:
        return a
    elif b > 0:
        return sum(a + 1, b - 1)
    else: 
        return sum(a - 1, b + 1)
    
a = int(input())
b = int(input())
print(sum(a, b))

# Примеры
# входные данные
# 2
# 2
# выходные данные
# 4