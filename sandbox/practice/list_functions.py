# Повидать мир: вспомните хотя бы пять стран, в которых вам хотелось бы побывать.
# sort, sorted, reverse

import os

# code begins
clear = lambda: os.system('cls')
clear()

country = ["Canada", "USA", "Tailand", "China", "Japan"]
print("Original list: ")
print(country)

print("Sorted list: ")
print(sorted(country))

print("Sorted reverse list: ")
print(sorted(country, reverse=True))

print("Reversed list: ")
country.reverse()
print(country)

print("Sorted by alphabet list: ")
country.sort()
print(country)