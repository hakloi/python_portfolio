w1 = 'horse'
w2 = 'ros'

m = len(w1)  # строки
n = len(w2)  # столбцы

dp = [[0] * (n + 1) for _ in range(m + 1)]

# Инициализация
for i in range(m + 1):
    dp[i][0] = i
for j in range(n + 1):
    dp[0][j] = j

# Заполнение таблицы
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if w1[i - 1] == w2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
            print("equal", w1[i - 1], w2[j - 1], dp[i][j])
        else:
            dp[i][j] = 1 + min(
                dp[i - 1][j],    # удаление
                dp[i][j - 1],    # вставка
                dp[i - 1][j - 1] # замена
            )
            print("not", w1[i - 1], w2[j - 1], dp[i][j])

# Вывод финальной таблицы
for row in dp:
    print(row)
