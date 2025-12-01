import numpy as np

def solve(n, m, A, B):
    # Преобразуем матрицы A и B в numpy массивы для удобства работы
    A = np.array(A)
    B = np.array(B)
    
    # Ищем решение с использованием линейной алгебры
    # Для того чтобы создать неоднозначность на выходе softmax, используем факт
    # что два значения в выходном векторе должны быть равными.
    # Мы будем решать задачу оптимизации с минимизацией разницы между максимальными значениями в выходном векторе.
    
    # Пробуем случайные векторы
    for i in range(1000):
        x = np.random.randn(n)  # случайный вектор
        x /= np.linalg.norm(x)  # нормируем его
        x_prime = A.dot(x)  # линейное преобразование первого слоя
        x_prime = np.maximum(x_prime, 0)  # ReLU активация
        y = B.dot(x_prime)  # линейное преобразование второго слоя
        softmax_y = np.exp(y - np.max(y))  # softmax
        softmax_y /= np.sum(softmax_y)  # нормируем на единицу
        
        if len(np.unique(softmax_y)) < m:  # если есть одинаковые максимальные вероятности
            return "YES", x.tolist()

    return "NO", []

# Чтение входных данных
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]

# Решение задачи
result, vector = solve(n, m, A, B)
if result == "YES":
    print(result)
    print(" ".join(map(str, vector)))
else:
    print(result)
