# Подсчитайте количество слов во входных данных.
# В этой задаче словом будет считаться любая последовательность
# строчных букв. Например, «привет» — это слово, но и всякие
# бессвязные наборы букв вроде «sdfsdf» тоже считаются словами.
# Входными данными будет одна строка текста, состоящая из строчных
# букв и пробелов. Между каждой парой слов будет ровно один пробел,
# при этом перед первым словом и после последнего слова их не будет.
# Максимальная длина строки — 800 символов.

# cleaner
import os

clear = lambda: os.system('cls')
clear()

# code begins
def intro (name):
    num = int(input("Welcome, " + name + "!" +
          "\nDo you want to try this app?" +
          "\n   1. Yes" + "\n   2. No\n"))
    if num == 1:
        phrase = input("Let's game begim!\nWrite something: ")
        print("Counter: ", len(phrase.split(" ")))
        
    else:
        print("I hope you will change your mind later!")
    
name = input("Name: ")
intro(name)


