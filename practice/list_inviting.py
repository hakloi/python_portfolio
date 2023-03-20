# Список гостей: если бы вы могли пригласить кого угодно (из живых или умерших) 
# на обед, то кого бы вы пригласили? Создайте список, включающий минимум трех людей, 
# которых вам хотелось бы пригласить на обед . Затем используйте этот список для вывода 
# пригласительного сообщения каждому участнику

import os

# code begins
clear = lambda: os.system('cls')
clear()

print("###############- 1 -###############")
l1 = ["Vainona Raider", "Johny Clo", "Barbara Gordon"]

def invitings(l1):
    for el in l1:
        print("Dear " + el +",\nI want to invite you in my party tonight!\n")
        
invitings(l1)

# Изменение списка гостей: вы только что узнали, что один из гостей прийти не сможет, 
# поэтому вам придется разослать новые приглашения . Отсутствующего гостя нужно
# заменить кем-то другим.
print("###############- 2 -###############")

removed_guest = "Johny Clo"
l1.remove(removed_guest)

print("Sorry, but guest "+ removed_guest+ " can't go to your party.\n")

l1.append("Kira Love")
invitings(l1)

# Больше гостей: вы решили купить обеденный стол большего размера . Дополнительные 
# места позволяют пригласить на обед еще трех гостей 
print("###############- 3 -###############")
print("Congratulations! Our dinner table allows to extend inviting's list!\n")

l1.insert(0, "Kylie Jenner")
l1.insert(3, "Cortny Kardashian")
l1.append("Lupa Pupa")

invitings(l1)

# Сокращение списка гостей: только что выяснилось, что новый обеденный стол
# привезти вовремя не успеют, и места хватит только для двух гостей
print("###############- 4 -###############")

lenght = len(l1)
while (lenght > 2 ):
    l1.pop(0)
    lenght = lenght - 1
print("New list of guests:\n")
invitings(l1)

del l1[1]
del l1[0]

print(l1)