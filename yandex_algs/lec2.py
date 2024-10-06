def rle(s):
    counter = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            counter += 1
        else:
            if counter == 1:
                print(f"{s[i - 1]}", end='')
                counter = 1
            else:
                print(f"{s[i - 1]}{counter}", end='')
                counter = 1
    if counter == 1:
        print(f"{s[-1]}", end='')
    else:
        print(f"{s[-1]}{counter}", end='')

s = input()
# s = 'aaabbc'
rle(s)
