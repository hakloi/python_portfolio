# num = int(input())
# results = list(map(int, input().split()))

# best_candidate = -1

# for i in range(1, num - 1):
#     if results[i] % 10 == 5 and results[i] > results[i + 1]:
#         best_candidate = max(best_candidate, results[i])

# if best_candidate == -1:
#     print(0)
# else:
#     place = 1 + sum(1 for x in results if x > best_candidate)
#     print(place)
    
num = int(input())
results = list(map(int, input().split()))

candidates = []
for i in range(1, num - 1):
    if results[i] % 10 == 5 and results[i] > results[i + 1]:
        candidates.append(results[i])

if not candidates:
    print(0)
else:
    best_candidate = max(candidates)
    place = 1 + sum(1 for x in results if x > best_candidate)
    print(place)
