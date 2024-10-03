# 4 15 17 2
# 30 2 1 3
# 47 3 2 3 4
# выходные данные
# 2
# 2 4 

# Чтение входных данных
bought_rubies, a_carat, b_carat, K = map(int, input().split())

# Список взвешиваний
weighings = []

for _ in range(K):
    data = list(map(int, input().split()))
    wi = data[0]  # общий вес в этом взвешивании
    mi = data[1]  # количество рубинов в взвешивании
    rubies = data[2:]  # номера рубинов
    weighings.append((wi, rubies))

# Инициализация множества возможных кандидатов на роль настоящих рубинов
possible_rubies = set(range(1, bought_rubies + 1))

# Обработка каждого взвешивания
for wi, rubies in weighings:
    total_a_weight = a_carat * len(rubies)  # Это вес, если все рубины поддельные
    
    # Минимальный и максимальный возможный вес набора
    min_possible_weight = total_a_weight  # все поддельные
    max_possible_weight = total_a_weight - a_carat + b_carat  # один поддельный заменен на настоящий

    # Если общий вес не попадает в диапазон возможных весов, выводим Impossible
    if wi < min_possible_weight or wi > max_possible_weight:
        print("Impossible")
        exit()  # Завершаем программу

    # Множество возможных кандидатов на роль настоящих рубинов для текущего взвешивания
    possible_in_this_weighing = set()

    # Проверяем, может ли каждый рубин в наборе быть настоящим
    for ruby in rubies:
        # Если заменив этот рубин на настоящий, вес совпадает с wi
        if total_a_weight - a_carat + b_carat == wi:
            possible_in_this_weighing.add(ruby)

    # Пересекаем с общим множеством возможных кандидатов
    possible_rubies &= possible_in_this_weighing

# Если после всех взвешиваний не осталось возможных кандидатов
if not possible_rubies:
    print("Fail")
else:
    # Выводим количество возможных кандидатов и их номера
    print(len(possible_rubies))
    print(*possible_rubies)
