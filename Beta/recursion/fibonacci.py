# def fibonacci(num):
#     # lst = [el[] for el in range(0, num + 1)]
#     lst = []
#     for i in range(0, num):
#         if i == 0 or i == 1:
#             lst.append(i)
#         else:
#             lst.append(lst[i - 1] + lst[i - 2])
#     yield " ".join(str(el) for el in lst)
    
def fibonacci(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b    

print(*fibonacci(5))
print(*fibonacci(10), sep=', ')