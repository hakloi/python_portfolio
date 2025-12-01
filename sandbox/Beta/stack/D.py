def deletion(s):
    stack = []
    cnt = 0
    
    for el in s:
        if el == "(":
            stack.append(el)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else: 
                cnt += 1
    return cnt + len(stack)

s = input()
print(deletion(s))