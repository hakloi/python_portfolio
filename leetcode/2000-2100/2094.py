from collections import Counter


def findEvenNumbers(digits):
    result = set()
    digit_count = Counter(digits)

    even = [_ for _ in range(100, 1000, 2)]

    for e in even:
        digits_of_e = [int(d) for d in str(e)]
        if not Counter(digits_of_e) - Counter(digit_count):
            result.add(e)
        
    return sorted(result)
    
print(findEvenNumbers([2,1,3,0]))
