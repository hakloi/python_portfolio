# Дана строка, в которой буква h встречается минимум 
# два раза. Удалите из этой строки первое и последнее 
# вхождение буквы h, а также все символы, находящиеся между ними.

# s = input()
s = 'In the hole in the ground there lived a hobbit'
# In tobbit

first_h = s.find('h')
last_h = s.rfind('h')

print(s[:first_h] + s[last_h:])