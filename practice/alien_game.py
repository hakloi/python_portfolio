import os

# code begins
clear = lambda: os.system('cls')
clear()

hp = 10

match hp:
    case 10:
        print("Green")
    case 5:
        print("Yellow")
    case 0:
        print("Red")
