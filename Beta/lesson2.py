# if elif else 
import os
os.system('cls') #clear

print("Введите первую и последнюю буквы русского алфавита.")
first_letter = input()
last_letter = input()
if (first_letter == "а" or first_letter == "А") and (
        last_letter == "я" or last_letter == "Я"):
    print("Верно.")
else:
    print("Неверно.")
