import os
os.system('cls')

# 1
# s = '12'
# print(f"{'12':0>10}") # withot using s 

# print(s.ljust(10, '='))

# 2
# s = 'hello my friend'
# print(s.lstrip('ehl')) # from start
# print(s.rstrip('enid')) # from end

# 3
# s = "hello,world,my,darling"
# print(s.split(',')) #create list, split elements by seporation 

# 4
# id_num = "16"
# print(id_num.zfill(5))
# print(id_num.zfill(10))
# print(id_num.zfill(15))

# СПИСКИ
# nums = [10, 20, 30, 40, 50]
# print(nums[0:2]) # [0,2)
# print(nums[:-2]) 
# print(nums[::-1]) # visa versa
# print(nums[::3]) # step 


# numbers = [10, 20, 30, 40, 'yex']
# print(numbers)
# print(type(numbers))

# nums = []
# for i in range(11): 
#     nums.append(int(i))
# print(nums)

# del nums[::2]
# print(nums)

# the tuple

# mixed = (1, 2, 'hello')
# print(mixed)

# one_number = (1, )
# print(type(one_number))

text = "Привет, мир!"
list_symbols = list(text)
tuple_symbols = tuple(text)
text_from_list = str(list_symbols)
print(list_symbols)
print(tuple_symbols)
print(text_from_list)