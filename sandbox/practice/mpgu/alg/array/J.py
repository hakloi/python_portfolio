# def theBiggest(points):
#     the_biggest = int(points[0])
#     for point in points:
#         if int(point) > the_biggest:
#             the_biggest = int(point)
#     return str(the_biggest)

# sportsmen = int(input())
# points = input().replace(" ", "")
# new_points = points.replace(theBiggest(points), '')

# print(theBiggest(new_points))

sportsmen = int(input())
points = map(int, input().split())
max_point, second_point = 0, 0

for point in points:
    if point > max_point:
        second_point = max_point
        max_point = point
    elif max_point > point > second_point:
        second_point = point
        
print(second_point)

# Выходные данные
# Требуется вывести одно число – результат Василия

# Примеры
# входные данные
# 5
# 4 3 3 1 2 
# выходные данные
# 3
# входные данные
# 8
# 1 2 5 3 5 6 6 5 
# выходные данные
# 5