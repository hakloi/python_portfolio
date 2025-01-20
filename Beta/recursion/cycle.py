def cycle(lst):
    while True:
        for item in lst:
            yield item
    
print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))