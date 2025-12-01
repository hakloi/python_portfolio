def answer(func):
    def wrapper(*args,**kwargs):
        res = func(*args, **kwargs)
        return f"Результат функции: {res}"
    return wrapper

@answer
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5))
print(a_plus_b(7, 9))