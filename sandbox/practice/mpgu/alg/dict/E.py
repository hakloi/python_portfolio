counter_dict = {}

with open('input.txt', 'r') as f:
    for line in f:
        text = line.split()
        pointer = 1
        for word in text:
            if word in counter_dict:
                counter_dict[word] += pointer
            else:
                counter_dict[word] = pointer

max_count = max(counter_dict.values())

max_words = []
for word, count in counter_dict.items():
    if count == max_count:
        max_words.append(word)
        
print(min(max_words))
