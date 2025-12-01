native_americans = {}
city_to_country = {}

n = int(input())
for i in range(n):
    cities = input().split()
    country = cities.pop(0)
    native_americans[country] = cities
    
    for city in cities:
        city_to_country[city] = country
    
m = int(input())
for j in range(m):
    request = input()
    
    if request in city_to_country:
        print(city_to_country[request])
    

# 2
# Aztec Tenochtitlan
# Inca Cusco Chan-Chan Tiwanaku
# 3
# Cusco
# Tenochtitlan
# Chan-Chan

# выходные данные
# Inca
# Aztec
# Inca