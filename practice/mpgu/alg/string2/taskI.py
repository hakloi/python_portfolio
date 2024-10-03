# Дана строка. Измените регистр символов в этой строке так, 
# чтобы первая буква каждого слова была заглавной, а остальные буквы - строчными.

# Решение оформите в виде функции Capitalize (S), возвращающей новую строку.

def Capitalize(s):
    newphrase = ''
    currentword = ''
    for el in s:
        if el.isalpha():
            currentword += el
        else: 
            currentword = 
            currentword = ''

    return newphrase
    


s = input()
print(LongestWord(s))
