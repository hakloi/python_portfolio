def isPalindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    
    return True

s = input()
res = isPalindrome(s)
if res:
    print('YES')
else: 
    print("NO")
