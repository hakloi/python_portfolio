n = int(input())

st = []
pr = []
res = []

for _ in range(n):
    op = input()
    
    if op == "-":
        print(st[-1])
        st.pop()
        pr.pop()
    elif op[0] == "+":
        x = int(op[1:])
        if len(st) == 0:
            st.append(x)
            pr.append(x)
        else:
            st.append(x)
            pr.append(pr[-1] + x)
    else:
        x = int(op[1:])
        if x == len(st):
            print(pr[-1])
        else:
            print(pr[-1] - pr[-x - 1])