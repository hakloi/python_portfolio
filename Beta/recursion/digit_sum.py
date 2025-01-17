def recursive_digit_sum(n):
    if n == 0:
        return 0
    else: 
        rem = n % 10
        n = n // 10
        
    return rem + recursive_digit_sum(n)

result = recursive_digit_sum(7321346)
print(result)