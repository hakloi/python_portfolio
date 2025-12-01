def generateParenthesis(n):
    res = []
    def func(op, cl, s):
        if len(s) == n * 2:
            res.append(s)
            print(s)
            return
        
        if op < n:
            func(op + 1, cl, s + '(')
            
        if cl < op:
            func(op, cl + 1, s + ')')
            
    func(0, 0, '')
    return res

print(generateParenthesis(3))