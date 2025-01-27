def merge(a, b):
    
    try:
        iter(a)
        iter(b)
    except TypeError:
        raise StopIteration
    
    if not all(isinstance(x, type(next(iter(a)))) for x in a) or not all(isinstance(x, type(next(iter(b)))) for x in b):
        raise TypeError
    
    if list(a) != sorted(a) or list(b) != sorted(b):
        raise ValueError
    
    return iter(sorted(a + tuple(b)))

print(*merge(35, (1, 2, 3)))