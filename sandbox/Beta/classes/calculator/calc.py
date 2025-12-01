lst = [1, 11, 2, 4, 6, 45]

# запись файла
with open("results.txt", "w", encoding="utf-8") as f:
    for el in lst:
        f.write(str(el) + '\n')