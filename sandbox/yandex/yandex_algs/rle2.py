def rle(s):
    result = []
    counter = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            counter += 1
        else:
            if counter == 1:
                result.append(s[i - 1])
            else:
                result.append(f"{s[i - 1]}{counter}")
            counter = 1
    if counter == 1:
        result.append(s[-1])
    else:
        result.append(f"{s[-1]}{counter}")
    
    print(''.join(result))

s = input()
rle(s)
