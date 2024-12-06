# def make_list(lenght, value=0):
#     return [value for _ in range(lenght)]

# result = make_list(3)
# result1 = make_list(5, 1)

# print(result, result1)

# def make_matrix(size, value=0):
#     if isinstance(size, int):
#         size = [size, size]
#     return [[value for _ in range(size[0])] for _ in range(size[1])]

# result = make_matrix(3)
# result1 = make_matrix((4, 2), 1)
# print(result, result1)


def gcd(*nums):
    def euclidean(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    res = nums[0]
    for num in nums[1:]:
        res = euclidean(res, num)
        
    return res

result = gcd(3)
result1 = gcd(36, 48, 156, 100500)
print(result, result1)
