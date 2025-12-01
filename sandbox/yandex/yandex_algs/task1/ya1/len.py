def format_text(text):
    words = text.split()
    max_len = max(len(word) for word in words) * 3
    formatted_text = ""
    current_line = ""
    for i, word in enumerate(words):
        if word.endswith(","):
            word = word[:-1] + " "
        else:
            word += " " if i != len(words) - 1 else ""
        if len(current_line) + len(word) <= max_len:
            current_line += word
        else:
            formatted_text += current_line.rstrip() + "\n"
            current_line = word
    formatted_text += current_line.rstrip()
    return formatted_text

# Чтение текста из input.txt или стандартного ввода
try:
    with open("input.txt", "r") as file:
        text = file.read().strip()
except FileNotFoundError:
    text = input().strip()

# Форматирование текста
formatted_text = format_text(text)

# Вывод отформатированного текста в output.txt или стандартный вывод
try:
    with open("output.txt", "w") as file:
        file.write(formatted_text)
except FileNotFoundError:
    print(formatted_text)