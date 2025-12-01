def get_value(item):
    return item[1]


n = int(input())

part = {x.split()[0]: int(x.split()[1]) for x in (input() for _ in range(n))}

sorted_participants = sorted(part.items(), key=get_value, reverse=True)
for name, _ in sorted_participants:
    print(name)

# 3
# Ivanov 15
# Petrov 10
# Sidorov 20