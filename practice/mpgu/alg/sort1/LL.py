# Дана строка, содержащая цифры и английские буквы (большие и маленькие). Найти и вывести количество цифр.

# Входные данные
# Вводится строка ненулевой длины. Известно также, что длина строки не превышает 1000 знаков.

# Выходные данные
# Выведите количество цифр, которые присутствуют в строке.

def count_nums(s, nums):
    if s == '':
        return nums
    
    if s[0].isnumeric():
        nums += 1
    return count_nums(s[1:], nums)


s = input()
print(count_nums(s, 0))
# Примеры
# входные данные
# 74kz31n8pn26f2iv10c7u8x356gl73jlka67i929z08i5mnn35h0n
# выходные данные
# 28