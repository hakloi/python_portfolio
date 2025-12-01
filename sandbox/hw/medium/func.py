# Напишите функцию sum_range(start, end), которая суммирует все целые числа
# от значения «start» до величины «end» включительно. 
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

import getpass
import shutil
# cleaner
import os

clear = lambda: os.system('cls')
clear()

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
def sum_range(start, end):
    sum = 0
    if start < end:
        for num in range(start, end+1):
            # print(num) - for checking
            sum = sum + num
    elif start > end:
        for num in range(end, start+1):
            sum = sum + num
    elif start == end:
        sum = start
    else:
        print("Sorry, we can't count it!")
        
    print("Congrats! The sum of range between {0} and {1} = {2}".format(start, end, sum))
        
# ---------------------------------------------------------
print("ACCESS DENIED".center(shutil.get_terminal_size().columns) +
             "YOUR NAME:".center(shutil.get_terminal_size().columns))

name = getpass.getpass("haha i hide your name...") #ТЕКСТ НЕВИДНО ОЧ КРУТО !!!!!
# ---------------------------------------------------------

start = int(input("Start number: "))
end = int(input("End number: "))
sum_range(start, end)

lst = list(name)
cool_name = ""
for el in lst:
    cool_name = cool_name + el + "☠"
print("Will see you soon, " + color.BOLD + cool_name + color.END)