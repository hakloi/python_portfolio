from sys import stdin
from collections import Counter

data = stdin.read().split()
n = int(data[0])
fragments = data[1:]

marker_sets = Counter()
for frag in fragments:
    unique_markers = frozenset(frag)
    marker_sets[unique_markers] += 1

total_pairs = n * (n - 1) // 2
incompatible = 0
sets = list(marker_sets.items())

for i in range(len(sets)):
    set1, count1 = sets[i]
    for j in range(i + 1, len(sets)):
        set2, count2 = sets[j]
        if set1.isdisjoint(set2):
            incompatible += count1 * count2

print(total_pairs - incompatible)
