def isValid(s):
    stack = []
    matching = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for el in s:
        if el in "{[(":
            stack.append(el)
        elif el in ")]}":
            if not stack or stack[-1] != matching[el]:
                return "no"
            stack.pop()
            
    return "yes" if not stack else "no"

s = input().strip()
print(isValid(s))
