from collections import deque

def goblin_queue(queries):
    left = deque()
    right = deque()
    result = []

    for query in queries:
        if query[0] == '+':
            right.append(query[1])
        elif query[0] == '*':
            right.appendleft(query[1])
        else:
            result.append(left.popleft())

        if len(left) < len(right):
            left.append(right.popleft())

    return result

n = int(input())
queries = []
for _ in range(n):
    parts = input().split()
    if parts[0] == '-':
        queries.append(('-',))
    else:
        queries.append((parts[0], int(parts[1])))

answers = goblin_queue(queries)
for ans in answers:
    print(ans)
