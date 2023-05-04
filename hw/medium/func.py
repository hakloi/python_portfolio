# Напишите функцию sum_range(start, end), которая суммирует все целые числа
# от значения «start» до величины «end» включительно. 
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

# cleaner
import os

clear = lambda: os.system('cls')
clear()

# code begins
def sum_range(start, end):
    sum = 0
    if start > end:
        print("")
    elif start < end:
        print("")
    elif start == end:
        sum = start
    else:
        print("Sorry, we can't count it!")
    print("Congrats! The sum of range between {0} and {1} = {2}".format(start, end, sum))
        
    
start = int(input("Start number: "))
end = int(input("End number: "))