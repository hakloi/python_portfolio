def validPalindrome(s):
    def is_palindrome_range(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    
    n = len(s)
    l, r = 0, n - 1
    while l < r:
        if s[l] != s[r]:
            return is_palindrome_range(l + 1, r) or is_palindrome_range(l, r - 1)
        l += 1
        r -= 1
        
    return True
            
print(validPalindrome("koolmook"))