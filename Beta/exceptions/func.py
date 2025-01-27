def only_positive_even_sum(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError
    
    if a <= 0 or b <= 0 or a % 2 != 0 or b % 2 != 0:
        raise ValueError
    
    return a + b
            
            
print(only_positive_even_sum("3", 2.5))