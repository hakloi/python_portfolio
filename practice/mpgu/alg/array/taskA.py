# Напишите программу, которая определяет, сколько раз встречается заданное число x в данном массиве.

# Входные данные
# В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива.

# Во второй строке вводятся N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).

# В третьей строке содержится одно целое число x , не превосходящее по модулю 1000.

# Выходные данные
# Вывести одно число – сколько раз встречается x в данном массиве.

n = int(input())
array = list(input().split())
target = input()

print(array.count(target))