# Алиса, Боб и Чарли хотят скинуться и купить подписку на Netflix.
# Однако Netfix позволяет использовать подписку только двум пользователям.
# Учитывая, что Алиса, Боб и Чарли имеют X, Y, Z денег соответственно и
# стоимость подписки на Netflix задана как COST денег. Напишите функцию,
# с определением кто может купить подписку (сумма каких двух чисел дает
# максимальное приближение к  COST). Известно, что X+Y+Z точно больше COST.

import os

# code begins
clear = lambda: os.system('cls')
clear()

def follow_netflix(x,y,z,cost):
    print("\nSubscription costs:", cost)
    if (x+y >= cost):
        print("Alice and Bob have",x+y,"so they buy it." )
    elif (x+z >= cost):
        print("Alice and Charlie have",x+z,"so they buy it.")
    elif (y+z >= cost):
        print("Bob and Charlie have",y+z,"so they buy it.")
    else:
        # в задании написано: что X+Y+Z точно больше COST
        # однако если мы вводим input , то предугадать такое неваозможно
        # поэтому стоит прописать вариант для варианта когда сумма трех меньше cost
        print("No one can buy it! Their sum is", x+y+z)

x = int(input("Alice's piece: "))
y = int(input("Bob's piece: "))
z = int(input("Charlie's piece: "))
cost = 100

follow_netflix(x,y,z,cost)
