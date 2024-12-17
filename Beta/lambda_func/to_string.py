def to_string(*data, sep=" ", end="\n"):
    return sep.join(str(_) for _ in data) + end


data = [7, 3, 1, "hello", (1, 2, 3)]
result = to_string(*data, sep=", ", end="!")
print(result)