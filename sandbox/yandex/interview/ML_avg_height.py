from collections import deque, defaultdict
import sys

input = sys.stdin.readline

n = int(input())
queue = deque()
height_count = defaultdict(int)
total_sum = 0

output = [] 

for _ in range(n):
    line = input()
    
    if line[0] == '+':
        _, k = line.split()
        k = int(k)
        queue.append(k)
        total_sum += k
        height_count[k] += 1
    else:  # '-'
        removed = queue.popleft()
        total_sum -= removed
        height_count[removed] -= 1
        if height_count[removed] == 0:
            del height_count[removed]
    
    if len(queue) == 0:
        output.append('0\n')
    elif total_sum % len(queue) != 0:
        output.append('0\n')
    else:
        avg = total_sum // len(queue)
        output.append(f"{height_count.get(avg, 0)}\n")

sys.stdout.write(''.join(output))
