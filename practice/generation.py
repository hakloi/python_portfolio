import os
import shutil

# some intresting features
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# code begins
clear = lambda: os.system('cls')
clear()

def exception_num(value):
    while True:
        try:
            num = int(value) # пробуем перевести в число, если не удается переходим в except
            break
        except :
            if value.isalpha(): # функция isalpha возвращает True если все символы буквы
                print("Letters are not allowed. Try again!")
                value = input("Input: ")
            else:
                print("Incomprehensible characters!")
                value = input("Input: ")
    return int(value)
    
def exception_str(value):
    while True:
        try:
            s = str(value) # пробуем перевести в строку, если не удается переходим в except
            break
        except :
            if value.isdigit(): # функция isdigit возвращает True если все символы цифры
                print("Numbers are not allowed. Try again!")
                value = input("Input: ")
            else:
                print("Incomprehensible characters!")
                value = input("Input: ")
    return value.title()

def generation(age):
    if age < 2:
        print(color.PURPLE +cool_name + color.END +", you're a newborn! What are you doing here?")
    elif age >= 2 and age < 4: 
        print(color.GREEN +cool_name + color.END + ", you're a baby! What are you doing here?")
    elif age >= 4 and age < 13:
        print(color.CYAN +cool_name + color.END + ", you're a kiddo! Do your mother know what are tou doing?")
    elif age >= 13 and age < 20:
        print(color.BLUE +cool_name + color.END + ", you're a teenager! Wanna try to apply documents to FBI?")
    elif age >= 20 and age < 65:
        print(color.DARKCYAN +cool_name + color.END + ", you're an adult! Are you ready to serve the country?")
    elif age >= 65:
        print(color.YELLOW +cool_name + color.END + ", you're an elderly person! We accept all of ages above 20!")

def transform_name(name):
    lst = list(name)
    cool_name = ""
    for el in lst:
        cool_name = cool_name + el + "☠"
    return cool_name
# -------------------------------------------

print(color.BOLD + "WELCOME TO FBI, KIDDO!".center(shutil.get_terminal_size().columns) +
      "FILL IN THE INFORMATION BELOW!".center(shutil.get_terminal_size().columns) + color.END)

print("NAME:".center(shutil.get_terminal_size().columns))
name = input("Input: ")
name = exception_str(name)
cool_name = transform_name(name)

print("SURNAME:".center(shutil.get_terminal_size().columns))
surname = input("Input: ")
surname = exception_str(surname)

print("AGE:".center(shutil.get_terminal_size().columns))
age = input("Input: ")
age = exception_num(age)

generation(age)