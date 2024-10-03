s = input()
# выходные данные
# In th a devil ereht dnuorg eht ni eloh ehobbit

first_h = s.find('h')
last_h = s.rfind('h')
res = s[first_h + 1 :last_h]
print(s[:first_h + 1] + res[::-1] + s[last_h:])
# print(res)
