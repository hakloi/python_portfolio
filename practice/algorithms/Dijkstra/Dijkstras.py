
 
from heapq import heapify, heappush
import sys

import os

# code begins
clear = lambda: os.system('cls')
clear()

def dijkstra(graph, src, dest):
    inf = sys.maxsize
    node_data = {'A':{'cost':inf, 'pred':[]},
                 'B':{'cost':inf, 'pred':[]},
                 'C':{'cost':inf, 'pred':[]},
                 'D':{'cost':inf, 'pred':[]},
                 'E':{'cost':inf, 'pred':[]},
                 'F':{'cost':inf, 'pred':[]}
                 }
    #initial node costs 0
    node_data[src]['cost'] = 0
    visited = []
    #will change when we go toward by graph
    temp = src
    for i in range(5):
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + list(temp)
                    heappush(min_heap,(node_data[j]['cost'],j))
        heapify(min_heap)
        temp = min_heap[0][1]
    print("Shortest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred'] +list(dest)))
    
if __name__ == "__main__":
    graph = {
            'A':{'B':2,'C':4},
            'B':{'A':2,'C':3,'D':8},
            'C':{'A':4,'B':4,'E':5,'D':2},
            'D':{'B':8,'C':4,'E':11,'F':22},
            'E':{'C':5,'D':11,'F':1},
            'F':{'D':22,'E':4}
        }
    
source = 'A'
destination = 'F'
dijkstra(graph,source,destination)