from sys import stdin

c = int(stdin.readline())
city_rooms = dict()

for _ in range(c):
    parts = stdin.readline().split()
    city = parts[0]
    n = int(parts[1])
    rooms = []
    for _ in range(n):
        schedule, name = stdin.readline().split()
        rooms.append((name, schedule))
    city_rooms[city] = rooms

m = int(stdin.readline())

for _ in range(m):
    parts = stdin.readline().split()
    l = int(parts[0])
    cities = parts[1:]

    found = False
    for h in range(24):
        used_rooms = []
        for city in cities:
            room_found = None
            for name, schedule in city_rooms[city]:
                if schedule[h] == '.':
                    room_found = name
                    break
            if room_found is None:
                break  
            used_rooms.append(room_found)
        else:
            print('Yes', *used_rooms)
            found = True
            break

    if not found:
        print('No')