# Требуется отсортировать массив по неубыванию методом "выбор максимума".

# Входные данные
# В первой строке вводится одно натуральное число, не превосходящее 1000 – размер массива. 
# Во второй строке задаются N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).

n = int(input())
nums = list(map(int, input().split()))

for i in range(n - 1, 0, -1):  
    max_ind = 0  
    for j in range(1, i + 1):  
        if nums[j] > nums[max_ind]:
            max_ind = j
    nums[i], nums[max_ind] = nums[max_ind], nums[i]

print(*nums)
# Выходные данные
# Вывести получившийся массив.

# Примеры
# входные данные
# 2
# 3 1
# выходные данные
# 1 3 