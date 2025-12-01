haystack = "sadbutsad"
needle = "sad"

if haystack.find(needle) != -1:
    start = haystack.find(needle)
    print(start)
else:
    print(-1)