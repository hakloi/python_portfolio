n, *h = list(map(int, input().split()))
lessR = [n] * n       
lessL = [-1] * n      
st = []

for i in range(n - 1, -1, -1):
    while st and h[st[-1]] >= h[i]:
        st.pop()
    if st:
        lessR[i] = st[-1]
    st.append(i)

st = []

for i in range(n):
    while st and h[st[-1]] >= h[i]:
        st.pop()
    if st:
        lessL[i] = st[-1]
    st.append(i)

max_area = 0
for i in range(n):
    width = lessR[i] - lessL[i] - 1  
    area = h[i] * width
    max_area = max(max_area, area)

print(max_area)
