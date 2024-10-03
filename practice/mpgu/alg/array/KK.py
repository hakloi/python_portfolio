days, parties = map(int, input().split())
strikes = set()

for party in range(parties):
    a, b = map(int, input().split())
    day = a
    
    # strikes.add(a)
    while day <= days:
        if (day % 7 != 6) and (day % 7 != 0):
            strikes.add(day)
        day += b


print(len(strikes))