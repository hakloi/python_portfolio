def recursive_sum(*args):
    if not args:
        return 0

    return args[0] + recursive_sum(*args[1:])
    
result = recursive_sum(1, 2, 3)
result1 = recursive_sum(7, 1, 3, 2, 10)
print(result, result1)