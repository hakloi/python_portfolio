import os
os.system('cls')
# Составить табличку функций строк в python (функция - пример использования - вывод)

#1
s = "hello, World!"
print(s.capitalize())

#2
w = 'hello'
print(w.isalpha())

#3
n = '8'
print(n.isdigit())

#4
s = "Hello, world!"
print(s.isalnum())

#5
print(s.isupper())

#6
print(s.islower())

#7
s = 'sdfllllllpofd'
print(s.count('l'))

#8
s = "Hello, world!"
print(s.find('l'))

#9
print(s.rfind('l'))

#10 - start-end
s = "Hello, world!"
print(s.endswith("world!"))
print(s.startswith("Hello"))

#11
s = 'hello'
print(s.replace('l', 'I'))

#12
s = "okay"
print(s.index("o"))

#13
s = "chichi"
print(s.ljust(10, "="))
print(s.rjust(10, "="))

#14
s = "Hello, World!"
print(s.lower())
print(s.upper())

#15
s = "dive into this!"
print(s.title())

#16
s = "7"
print(s.zfill(3))