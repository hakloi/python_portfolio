def ExtractDigits(s):
    news = ''
    for el in s:
        if el.isdigit():
            news += el
    return news

s = input()
print(ExtractDigits(s))