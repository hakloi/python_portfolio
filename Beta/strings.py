# length = int(input())
# count = int(input())

# for i in range(count):
#     word = input()
#     if len(word) > length:
#         shortened = word[:length - 3] + '...'
#         print(shortened)
#     else: 
#         print(word)


# Ввод
# Hello, world
# Hello, @@@
# ##Goodbye

# Вывод
# Hello, world
# Goodbye

# word = input()

# if word[:2] == '##':
#     newword = word[2:]
#     print(newword)
# elif word[-3:] == '@@@':
#     newword = ''
# else:
#     print(word)

# while True:
    
#     word = input()

#     if word == '':
#         break
#     if word[:2] == '##':
#         word = word[2:]

#     if word[-3:] == '@@@':
#         continue
#     print(word)

# s = input().lower()
# if s == s[::-1]:
#     print('YES')
# else:
#     print('NO')

# Очередное путешествие родителей с детьми, очередная игра с поиском зверушек за окном.
# Давайте поиграем и найдём заек.

# Формат ввода
# В первой строке записано натуральное число 
# 𝑁
# N — количество выделенных придорожных местностей.
# В каждой из 
# 𝑁
# N последующих строк записано описание придорожной местности.

# n = int(input())
# count = 0

# for i in range(n):
#     phrase = input()
#     count += phrase.count('зайка')

# print(count)

# s = input()
# a, b = s.split(' ')
# print(int(a) + int(b))

# n = int(input())

# for i in range(n):
#     phrase = input()
#     letter = phrase.find('зайка')
#     if letter != -1:
#         print(letter + 1)
#     else:
#         print('Заек нет =(')

# ---------------

# while True:
    
#     word = input()
#     pivot = word.find('#')

#     if word == '':
#         break
#     if pivot == 0:
#         continue
#     elif pivot != -1:
#         word = word[:pivot]
#         print(word)
#     else: 
#         print(word)

# ----------------

while True:
    
    word = input().lower()

    if word == 'ФИНИШ':
        break
    
