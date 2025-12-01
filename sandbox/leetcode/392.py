s = "axc"
t = "ahbgdc"

j = 0

while j != len(s):
    for i in range(len(t)):
        if t[i] == s[j]:
            j += 1
        if j == len(s):
            print(True)
            print(j)
    print(False)