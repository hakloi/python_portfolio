import json
from sys import stdin

f1 = input()

with open(f1, "r", encoding="utf-8") as filein:
    records = json.load(filein)

for line in stdin:
    a, b = line.replace(" ", "").split('==')
    records[a] = b.strip("\n")


with open(f1, "w", encoding="utf-8") as fileout:
    json.dump(records, fileout, ensure_ascii=False, indent=4)

# data.json
# one == один
# two == два
# three == три