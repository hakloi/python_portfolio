def Eval(s):
    num1 = ''
    num2 = ''
    oper = ''
    count = 0

    for el in s:
        if el.isdigit():
            num1 += el
            count += 1
        else:
            oper = el  
            break

    for el in s[count+1:]:
        if el.isdigit():
            num2 += el

    num1 = int(num1)
    num2 = int(num2)

    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2

s = input()
print(Eval(s)) 
