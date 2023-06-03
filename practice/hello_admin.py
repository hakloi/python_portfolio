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

current_users = ["Jeremy", "Walley", "Amanda", "Juno", "William", "Violet"]

def new_name(current_users):
    print("NAME:".center(shutil.get_terminal_size().columns))
    name = input("Input: ")
    for el in current_users:
        # case-insensitive
        if name.casefold() == el.casefold() : 
            print("You can't use this name!")
            return 0
        else:
            print("Welcome, " + color.BOLD + name + color.END)
            return name
        
name = new_name(current_users)     
