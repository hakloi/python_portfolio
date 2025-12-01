# from sys import stdin

# lines = stdin.read().strip().splitlines()
# lst = sum([sum(map(int, line.split())) for line in lines])

# print(lst)


# 1 2
# 3 4 5
# 6
# 7 8 9 10

# from sys import stdin

# lines = stdin.read().strip().splitlines()
# lst = [line.split()[1:] for line in lines]

# res = []
# for v in lst:
#     diff = abs(int(v[0]) - int(v[1]))
#     res.append(diff)
    
# result = round(sum(res) / len(res))
# print(result)
    
    
# from sys import stdin

# lines = stdin.read().strip().splitlines()

# res = []

# for line in lines:
#     line.split()
#     if "#" in line:
#         ind = line.index("#")
#         if ind != 0:
#             res.append(line[:ind].rstrip())
#     else:
#         res.append(line)
        
# print(*res, sep="\n")
        
        
# from sys import stdin

# lines = stdin.read().strip().splitlines()
# target = lines[-1]

# for line in lines:
#     if target.lower() in line.lower():
#         print(line)


# from sys import stdin

# lines = stdin.read().strip().splitlines()

# res = [line.split() for line in lines]

# result = []

# for v in res:
#     for i in v:
#         if i.lower() == i.lower()[::-1]:
#             result.append(i)

# result = sorted(list(set(result)))

# print(*result, sep="\n")


# alphabeth = {
#     'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z',
#     'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
#     'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Tc', 'Ч': 'Ch', 'Ш': 'Sh', 
#     'Щ': 'Shch', 'Ы': 'Y', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia',
#     'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z',
#     'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
#     'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'tc', 'ч': 'ch', 'ш': 'sh', 
#     'щ': 'shch', 'ы': 'y', 'э': 'e', 'ю': 'iu', 'я': 'ia',
#     'ъ': '', 'ь': '', 'Ъ': '', 'Ь': '' 
# }
    
# with open("cyrillic.txt", "r", encoding="utf-8") as filein, \
#      open("transliteration.txt", "w", encoding="utf-8") as fileout:
#     for line in filein:
#         translated = []
#         for char in line:
#             translated_char = alphabeth.get(char, char)
#             translated.append(translated_char)
#         fileout.write("".join(translated))

# from sys import stdin

# name = input()

# with open(name, "r", encoding="utf-8") as file:
#     lines = file.read().strip().splitlines()
#     lst = sum(list(line.split() for line in lines), [])

# res = [int(x) for x in lst]

# lenght = len(res)
# summa = sum(res)
# print(lenght)
# positive = [x for x in res if x > 0]
# print(len(positive))
# print(min(res))
# print(max(res))
# print(summa)
# print(f"{(summa / lenght):.2f}")

# 14
# 9
# -5
# 20
# 60
# 4.29

# f1 = input()
# f2 = input()
# f3 = input()

# with open(f1, "r", encoding="utf-8") as filein, \
#      open(f2, "r", encoding="utf-8") as filein2, \
#      open(f3, "w", encoding="utf-8") as fileout:
#          lst1 = set(sum([line.split() for line in filein], []))
#          lst2 = set(sum([line.split() for line in filein2], []))
#          res = sorted(lst1.symmetric_difference(lst2))
         
#          fileout.write("\n".join(res))
         

