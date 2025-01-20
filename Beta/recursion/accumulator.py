global res
res = []

def result_accumulator(func):
    def wrapper(*args, method="accumulate", **kwargs):
        res.append(func(*args, **kwargs))
        if method == "accumulate":
            return None
        elif method == "drop":
            acc_result = res[:]
            res.clear()
            return acc_result
        
    return wrapper
    
@result_accumulator
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))