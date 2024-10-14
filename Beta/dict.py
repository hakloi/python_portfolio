import os
os.system('cls')

# alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.',
#             'D': '-..', 'E': '.', 'F': '..-.',
#             'G': '--.', 'H': '....', 'I': '..',
#             'J': '.---', 'K': '-.-', 'L': '.-..',
#             'M': '--', 'N': '-.', 'O': '---',
#             'P': '.--.', 'Q': '--.-', 'R': '.-.',
#             'S': '...', 'T': '-', 'U': '..-',
#             'V': '...-', 'W': '.--', 'X': '-..-',
#             'Y': '-.--', 'Z': '--..',
#             '0': '-----', '1': '.----', '2': '..---',
#             '3': '...--', '4': '....-', '5': '.....',
#             '6': '-....', '7': '--...', '8': '---..',
#             '9': '----.'}

# s = input().upper()
# words = s.split()

# for word in words:
#     new_s = ' '.join(alphabet[char] for char in word if char in alphabet)
#     print(new_s)


# Ввод
# Hello world
# Вывод
# .... . .-.. .-.. ---
# .-- --- .-. .-.. -..


# friendships = {}

# while True:
#     pair = input()
#     if pair == '':  
#         break
    
#     person1, person2 = pair.split()  
    
#     if person1 not in friendships:
#         friendships[person1] = []
#     if person2 not in friendships:
#         friendships[person2] = []
    
#     friendships[person1].append(person2)
#     friendships[person2].append(person1)

# for person in sorted(friendships):
#     friends = friendships[person]
#     second_level_friends = set() 
    
#     for friend in friends:
#         for f_of_friend in friendships.get(friend, []):
#             if f_of_friend != person and f_of_friend not in friends:
#                 second_level_friends.add(f_of_friend)
    
#     if second_level_friends:
#         second_level_friends = sorted(second_level_friends)  
#         print(f"{person}: {', '.join(second_level_friends)}")
#     else:
#         print(f"{person}:") 

        
# Васильев: Иванов, Кириллов, Яковлев
# Иванов: Васильев, Кириллов, Яковлев
# Кириллов: Васильев, Иванов, Яковлев
# Петров: Сергеев
# Сергеев: Петров
# Яковлев: Васильев, Иванов, Кириллов


# ----------------------
# 9
# 10 18
# 17 15
# 25 21
# 0 21
# 1 16
# 25 29
# 24 24
# 8 26
# 10 20

n = int(input())
d = {}

for i in range(n):
    x, y = input().split()
    if len(x) == 2:
        trans = int(x) // 10
        if trans in d:
            d[trans] += [y]
        else:
            d[trans] = [y]

