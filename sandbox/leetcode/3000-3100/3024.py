from collections import Counter


def triangleType(nums):
    a, b, c = sorted(nums)
    
    if a + b <= c:
        return "none"
    
    if a == b and b == c and c == a:
        return "equilateral"
    elif a == b or b == c or c == a:
        return "isosceles"
    else:
        return "scalene"
    
    
print(triangleType([1, 2, 3]))
print(triangleType([1, 2, 2]))
print(triangleType([1, 1, 1]))