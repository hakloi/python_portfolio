# n = int(input())
# comparision = {}

# for i in range(n):
#     kid = input().split()
#     if len(kid) < 2:
#         continue
    
#     name = kid[0]
#     porridges = kid[1:] 
#     comparision[name] = porridges
    
# porridge = input()   

# targets = [i for i in comparision if porridge in comparision[i]]
# if targets == []:
#     print('Таких нет')
# else:
#     targets.sort()
#     print(*targets, sep='\n')
    
# 3
# Иванов манная овсяная
# Петров манная овсяная
# Васечкин манная овсяная
# м

# березка елочка зайка волк березка
# сосна зайка сосна елочка зайка медведь
# сосна сосна сосна белочка сосна белочка

count_dict = {}

while (words := input()) != "":
    list_words = words.split()
    point = 1
    for i in range(len(list_words)):
        if list_words[i] in count_dict:
            count_dict[list_words[i]] += 1
        else: 
            count_dict[list_words[i]] = point   
    
for key, value in count_dict.items():
  print("{0} {1}".format(key,value))