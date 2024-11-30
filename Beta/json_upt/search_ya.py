from sys import stdin

request = " ".join(input().lower().split())
txts = set()

for file in stdin:
    file = file.strip()
    with open(file, "r", encoding="utf-8") as txt_file:
        content = " ".join(txt_file.read().lower().split())
        
        if request in content:
            txts.add(file)


if not txts:
    print("404. Not Found")
else:
    res = sorted(list(txts))
    print(*res, sep="\n")