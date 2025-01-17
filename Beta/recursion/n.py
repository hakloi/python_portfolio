def make_equation(*coeffs):
    if len(coeffs) == 1:
        return f"({coeffs[0]})"
    
    return f"({make_equation(*coeffs[:-1])} * x + {coeffs[-1]})"

print(make_equation(3, 1, 5, 3))