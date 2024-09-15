
def CaesarCipher (s, k):
    if not s.isalpha():
        return s
    if s.isalpha():
        if s.isupper():
            position = ord(s) + k
            if position > ord('Z'):
                position = position - 26
            return chr(position) 
        elif s.islower():
            position = ord(s) + k
            if position > ord('z'):
                position = position - 26
            return chr(position) 

    

s = input()
for el in s:
    print(CaesarCipher(el, 3), end='')
# выходные данные
# Lq d kroh lq wkh jurxqg wkhuh olyhg d kreelw.