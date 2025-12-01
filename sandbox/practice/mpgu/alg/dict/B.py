with open('input.txt', 'r') as f:
    text = f.read()
    
words = text.split()

count_dict = {}
res = []

for word in words:
    point = 1
    if word in count_dict:
        count_dict[word] += point
        res.append(count_dict.get(word))
    else: 
        count_dict[word] = 0
        res.append(0)

print(*res)

# 0 0 0 0 0 0 1 0 0 1 0 0 1 0 2 2 0 0 0 0 1 2 3 3 1 1 4 0 1 0 1 2 4 1 5 0 0
# 0 0 0 0 0 0 1 0 0 1 0 0 1 0 2 2 0 0 0 0 1 2 3 3 1 1 4 0 1 0 1 2 4 1 5 0 0 