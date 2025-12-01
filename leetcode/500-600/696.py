# def countBinarySubstrings(s):
#     subs = []
#     res = 0
    
#     ln = 1
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             ln += 1
#         else: 
#             subs.append(ln)
#             ln = 1
#     subs.append(ln)
    
#     print(subs)
#     for j in range(1, len(subs)):
#         # print(subs[j], subs[j - 1])
#         res += min(subs[j], subs[j - 1])

#     return res
    
    
def countBinarySubstrings(s):
    prev = s[0]
    cnt = 1
    prev_cnt = 0
    res = 0
    
    for curr in s[1:]:
        if curr == prev:
            cnt += 1
        else:
            res += min(cnt, prev_cnt)
            prev_cnt = cnt
            cnt = 1
            prev = curr
    res += min(prev_cnt, cnt)
    
    return res 
s = "1111000"
print(countBinarySubstrings(s))