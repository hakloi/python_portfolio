import os
os.system('cls')


kids = int(input())
all_lans = set() #здесь которые знает хоть один школьник
common_lans = None #будем искать здесь общие всем известные

for i in range(kids):
    n_langs = int(input())
    languages = set() #текущий школьник
    
    for j in range(n_langs):
        idioma = input()
        languages.add(idioma) 
        all_lans.add(idioma)

    if common_lans is None:
        common_lans = languages
    else:
        common_lans &= languages
        
print(len(common_lans))
print(*common_lans, sep='\n')
print(len(all_lans))
print(*all_lans, sep='\n')