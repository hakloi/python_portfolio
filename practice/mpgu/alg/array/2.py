# Напишите программу, которая будет выполнять последовательность 
# запросов вида ADD num, PRESENT num и COUNT (без параметра). 
# Программу обязательно следует писать с использованием шаблонного типа set.

n = int(input())
current_set = set()

for i in range(n):
    operation = list(input().split())
    if 'ADD' in operation:
        current_set.add(operation[1])
    elif 'PRESENT' in operation:
        if operation[1] in current_set:
            print('YES')
        else: 
            print('NO')
    elif 'COUNT' in operation:
        print(len(current_set))


# входные данные
# 7
# ADD 5
# ADD 7
# COUNT
# PRESENT 3
# PRESENT 5
# ADD 3
# COUNT
# выходные данные
# 2
# NO
# YES
# 3