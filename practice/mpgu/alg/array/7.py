with open('input.txt', 'r') as file:
    text = file.read()

words = text.split()

unique_words = set(words)
print(len(unique_words))