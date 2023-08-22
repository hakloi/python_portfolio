from collections import deque
import os

# code begins
clear = lambda: os.system('cls')
clear()

# dictionary
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E', 'F'],
  'C' : ['G'],
  'D' : [],
  'E' : [],
  'F' : ['H'],
  'G' : ['I'],
  'H' : [],
  'I' : []
}

def bfs(graph, node):
    visited = []
    queue = deque() #double-ended queue 

    visited.append(node)
    queue.append(node)

    while queue:
        # popleft is O(1). for an array, pop(0) is O(n). hence the change to deque from array.
        s = queue.popleft()
        print(s, end = " ")

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

def main():
    bfs(graph, 'B')

main()