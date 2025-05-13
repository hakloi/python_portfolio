maxStars = 9 # int 
char = "*"

for i in range(maxStars, 0, -2):
  h = f'{char * i: ^{maxStars}}'
  print(h)
