# Напишите функцию search_substr(subst, st), которая принимает 2 строки
# и определяет, имеется ли подстрока subst в строке st. 
# В случае нахождения подстроки, возвращается фраза «Есть контакт!», а иначе «Мимо!». 
# Должно быть найдено совпадение независимо от регистра обеих строк.

import os
import random

# code begins
clear = lambda: os.system('cls')
clear()

def search(phrase, word):
    try:
        phrase.index(word)
    except ValueError:
        print("\nMissing! There is no similar word!")
    else:
        print("\nThere is this word!")

phrase = str(input("Write something: "))
word = str(input("Write one word from your phrase above: "))
search(phrase, word)