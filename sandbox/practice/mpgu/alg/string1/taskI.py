# Дана строка, в которой буква h встречается как минимум два раза. 
# Повторите последовательность символов, заключенную между первым 
# и последнием появлением буквы h два раза, сами буквы h повторять не надо.

s = input()
# выходные данные
# In the hole in the ground there lived a e hole in the ground there lived a hobbit
first_h = s.find('h')
last_h = s.rfind('h')
res = s[first_h + 1 :last_h]
print(s[:first_h + 1] + res * 2 + s[last_h:])