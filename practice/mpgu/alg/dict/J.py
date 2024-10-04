counter = {}

with open('input.txt', 'r') as f:
    for line in f:
        words = line.split()
        point = 1
        for word in words:
            if word in counter:
                counter[word] += point
            else:
                counter[word] = point

list_counter = [(k, v) for k, v in counter.items()]
    
list_counter.sort(key=lambda x: (-x[1], x[0]))

for word, freq in list_counter:
    print(word)
    
# damme
# is
# name
# van
# bond
# claude
# hi
# my
# james
# jean
# what
# your