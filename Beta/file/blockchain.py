n = int(input())

blocks = [int(input()) for _ in range(n)]


prev_h = 0
for i, b in enumerate(blocks):
    h = b % 256
    r = (b // 256) % 256
    m = b // (256**2)

    expected_h = (37 * (m + r + prev_h))  % 256 if i > 0 else (37 * (m + r)) % 256
    # print(f"Expected h: {expected_h}")
    if h != expected_h or h >= 100:
        print(i)
        break
    
    prev_h = h
else:
    print(-1)
    
