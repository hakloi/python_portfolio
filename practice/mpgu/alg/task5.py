s = input()
# s = 'jkdj'
find_f = s.find('f')
find_next_f = s.rfind('f', find_f + 1)

if find_f != -1:
    print(find_f, end=' ')
if find_next_f != -1:
    print(find_next_f, end=' ')

# s = 'dfgdfg dfgsdfg  dfgdgs'
