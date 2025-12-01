# print(ord('z'), ord('Z'), ord('a'), ord('A'))


# z = 122, Z = 90, a = 97, A = 65
# A -Z ->65 ... 90
# ord('A') <= ord(var) <= ord('Z')

def expression(user_input):
    exp = user_input.split()

    uno = ['~', '#', '!']
    duo = ['+', '-', '*', '/']
    trio = ['@']

    stack = []

    while exp != []:
        op = exp.pop(0)
        if op in uno:
            a = stack.pop()
            match op:
                case '~':
                    stack.append(-a)
                case '!':
                    res = 1
                    for i in range(1, a + 1):
                        res *= i
                    stack.append(res)
                case '#':
                    stack.append(a)
                    stack.append(a)
        elif op in duo:
            a = stack.pop()
            b = stack.pop()
            match op:
                case '+':
                    stack.append(b + a)
                case '-':
                    stack.append(b - a)
                case '*':
                    stack.append(b * a)
                case '/':
                    stack.append(b // a)
        elif op in trio:
            a = stack.pop()
            b = stack.pop()
            c = stack.pop()
            match op:
                case '@':
                    stack.append(b)
                    stack.append(a)
                    stack.append(c)
        else:
            stack.append(int(op))

    return int(stack[-1])
    

print(expression("3 4 5 + *"))