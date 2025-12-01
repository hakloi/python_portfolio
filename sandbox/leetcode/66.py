def plusOne(digits):
    digit = str(int("".join(str(_) for _ in digits)) + 1)
    return list(int(el) for el in digit)
    
    
digits = [1, 2, 3]
print(plusOne(digits))