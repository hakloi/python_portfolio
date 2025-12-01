# def isValid(s):
#     opening = ["{", "(", "["]
#     closing = ["}", ")", "]"]
#     stack = []

#     for el in s:
#         if el in opening:
#             stack.append(el)
#         elif el in closing and len(stack) >= 1:
#             if opening.index(stack[-1]) == closing.index(el):
#                 stack.pop()
#         else:
#             return False

#     if stack == []:
#         return True
#     else:
#         return False


# s = "]"
# print(isValid(s))

# OTHER WAY -------------------------------------------------
def isValid(s):
    dct = {"[": "]", "(": ")", "{": "}"}
    stack = []

    for el in s:
        if el in "{[(":
            stack.append(el)
        elif len(stack) == 0 or dct[stack.pop()] != el:
            return False

    return len(stack) == 0


s = "{]}"
print(isValid(s))
