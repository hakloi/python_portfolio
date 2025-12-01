import os

# code begins
clear = lambda: os.system('cls')
clear()

# Больше циклов: во всех версиях foods .py из этого раздела мы избегали использования 
# цикла for при выводе для экономии места . Выберите версию foods .py и напишите два цикла 
# for для вывода каждого списка .

def print_list(l1):
    for el in l1:
        print(el)

fav_pizza = ['meatball', 'cheese', 'pepperoni', 'with ananas']
friend_fav_pizza = fav_pizza[:]
friend_fav_pizza.append('fish and cream')

print('\nThis is my list of fav pizzas:')
print_list(fav_pizza)
print("\nThis is my friend's list of fav pizzas:")
print_list(friend_fav_pizza)