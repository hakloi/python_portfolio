# if elif else 
import os
os.system('cls') #clear

# saved_pwd = "qwerty"
# pwd = input("Введите пароль для входа: ")
# while pwd != saved_pwd:
#     pwd = input("Введите пароль для входа: ")
# print("Пароль верный.")

# saved_pwd = "qwerty"
# while input("Введите пароль для входа: ") != saved_pwd:
#     pass
# print("Пароль верный.")

# walrus operator (python 3.8)
# while (name := input("Введите имя: ")) != "ВЫХОД":
#     print(f"Привет, {name}!")
# print("Программа завершена.")

# name = input("Введите имя: ")
# while name != 'ВЫХОД':
#     print(f"Привет, {name}!")
#     name = input("Введите имя: ")
# print("Программа завершена.")


# for i in range(n)
# for i in range(5):
#     print(i)


s = int(input())
e = int(input())

if e > s:
    for el in range(e, s + 1):
        print(el, end=" ")
# elif 
else:
    for el in range(s, e + 1, -1):
        print(el, end=" ")
    