# from collections import defaultdict
# import heapq

# n, m = map(int, input().split())
# b = [int(input()) for _ in range(n)]

# type_to_objects = defaultdict(list)

# for i in range(n):
#     rel = 2 ** (-i)
#     type_to_objects[b[i]].append((rel, i))

# for t in type_to_objects:
#     type_to_objects[t].sort(reverse=True)

# heap = []
# for t, objs in type_to_objects.items():
#     if objs:
#         rel, idx = objs[0]
#         heapq.heappush(heap, (-rel, t, 0))  

# result = []
# last_type = -1  

# while heap:
#     temp = []
#     found = False

#     while heap:
#         neg_rel, t, pos = heapq.heappop(heap)
#         if t != last_type:
#             result.append(type_to_objects[t][pos][1])  
#             last_type = t
#             if pos + 1 < len(type_to_objects[t]):
#                 next_rel, next_idx = type_to_objects[t][pos + 1]
#                 heapq.heappush(heap, (-next_rel, t, pos + 1))
#             found = True
#             break
#         else:
#             temp.append((neg_rel, t, pos))

#     for item in temp:
#         heapq.heappush(heap, item)

#     if not found:
#         break

# print(' '.join(map(str, result)))


# 101 

# from collections import defaultdict, deque

# n, m = map(int, input().split())
# b = [int(input()) for _ in range(n)]

# type_queues = defaultdict(deque)
# for i in range(n):
#     type_queues[b[i]].append(i)

# active_types = set(t for t in type_queues if type_queues[t])

# result = []
# last_type = -1

# while True:
#     best_i = None
#     best_t = None
#     for t in active_types:
#         if t == last_type or not type_queues[t]:
#             continue
#         candidate = type_queues[t][0]
#         if best_i is None or candidate < best_i:
#             best_i = candidate
#             best_t = t

#     if best_t is None:
#         break

#     result.append(best_i)
#     type_queues[best_t].popleft()
#     if not type_queues[best_t]:
#         active_types.discard(best_t)
#     last_type = best_t

# print(' '.join(map(str, result)))


import heapq
from collections import deque

n, m = map(int, input().split())
b = [int(input()) for _ in range(n)]

type_queues = [deque() for _ in range(m)]
for i in range(n):
    type_queues[b[i]].append(i)

heap = []
for t in range(m):
    if type_queues[t]:
        heapq.heappush(heap, (type_queues[t][0], t))

result = []
last_type = -1

while heap:
    temp = []
    chosen = None
    while heap:
        i, t = heapq.heappop(heap)
        if t != last_type:
            chosen = (i, t)
            break
        else:
            temp.append((i, t))
    for item in temp:
        heapq.heappush(heap, item)

    if chosen is None:
        break

    i, t = chosen
    result.append(i)
    type_queues[t].popleft()
    if type_queues[t]:
        heapq.heappush(heap, (type_queues[t][0], t))
    last_type = t

print(' '.join(map(str, result)))
