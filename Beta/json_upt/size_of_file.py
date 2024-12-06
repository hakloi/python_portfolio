# бит (б)
# Байт (Б) = 8 бит
# Килобайт (КБ) = 1024 Б
# Мегабайт (МБ) = 1024 КБ
# Гигабайт (ГБ) = 1024 МБ

import os
import math as m

file = input()

size = os.path.getsize(file)
name = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
weight = 0

while size > 1024 and weight < len(name):
    weight += 1
    size, overload = divmod(size, 1024)
    size += int(overload > 0)

print(f"{size}{name[weight]}")