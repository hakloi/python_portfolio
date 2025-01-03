# Дана строка, содержащая только десятичные цифры. Найти и вывести наибольшую цифру.

# Входные данные
# Вводится строка ненулевой длины. Известно также, что длина строки не 
# превышает 1000 знаков и строка содержит только десятичные цифры.

# Выходные данные
# Выведите максимальную цифру, которая встречается во введенной строке.

def max_num(num, great):
    if num == 0:
        return great
    remainder = num % 10
    num = num // 10
    if great < remainder:
        great = remainder
    return max_num(num, great)

num = int(input())
great = int(str(num)[0])
print(max_num(num, great))

# Примеры
# входные данные
# 12345234
# выходные данные
# 5