n = int(input()) 
possible_numbers = set(range(1, n + 1))

while True:
    line = input()  
    if line == "HELP": 
        break
    
    current_set = set(map(int, line.split())) 
    
    answer = input()
    
    if answer == "YES": 
        possible_numbers &= current_set
    elif answer == "NO": 
        possible_numbers -= current_set

print(*sorted(possible_numbers))
# Примеры
# входные данные
# 10
# 1 2 3 4 5
# YES
# 2 4 6 8 10
# NO
# HELP