import os

# code begins
clear = lambda: os.system('cls')
clear()

# Нечетные числа: воспользуйтесь третьим аргументом функции range() для создания 
# списка нечетных чисел от 1 до 20 . Выведите все числа в цикле for 

print("\nList of odd numbers:")
odd_num = [print(num) for num in range(3,20,2)]

# Тройки: создайте список чисел, кратных 3, в диапазоне от 3 до 30 . Выведите все числа 
# своего списка в цикле for 

print("\nList of numbers that multiple of three:")
odd_num = [print(num) for num in range(3,30,3)]

# Кубы: результат возведения числа в третью степень называется кубом . Например, 
# куб 2 записывается в языке Python в виде 2**3 . Создайте список первых 10 кубов (то есть 
# кубов всех целых чисел от 1 до 10) и выведите значения всех кубов в цикле for 

print("\nList of cubic numbers:")
odd_num = [num**3 for num in range(1,10)]
print(list(odd_num))