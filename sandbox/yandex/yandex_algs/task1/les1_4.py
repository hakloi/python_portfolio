# check if a palindrom (skip space, no-sensitive for register)

n = str(input("Enter: "))

def palindrome(n):
    n = n.lower()
    n = ''.join(char for char in n if char.isalpha())
    if str(n) == str(n)[::-1]: print(True)
    else: print(False)


palindrome(n)

