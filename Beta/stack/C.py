# 8 9 + 1 7 - *

def polskiNotation(exp):
    stack = []
    
    for op in exp.split():
        if op in "+-/*":
            op1 = int(stack.pop())
            op2 = int(stack.pop())
            if op == "+":
                stack.append(op2 + op1)
            if op == "-":
                stack.append(op2 - op1)
            if op == "*":
                stack.append(op2 * op1)
            if op == "/":
                stack.append(op2 / op1)
        else:
            stack.append(op)
    return stack
    
exp = input().strip()
print(*polskiNotation(exp))