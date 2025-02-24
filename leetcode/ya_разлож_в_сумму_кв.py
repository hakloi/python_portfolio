def sum_of_squares(n):
    for i in range(2, int(n ** 0.5) + 1):
        b = n - (i ** 2)  

        if (b ** 0.5).is_integer():
            return i, int(b ** 0.5)
            
            
n = int(input())
print(*sum_of_squares(n))
