s = input()
# выходные данные
# In the Hole in tHe ground tHere lived a hobbit

first_h = s.find('h')
last_h = s.rfind('h')

print(s[:first_h + 1] + s[first_h + 1:last_h].replace('h', 'H') + s[last_h:])