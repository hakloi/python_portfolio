import sys
import heapq

MOD = 10**9 + 7

def main():
    m, n = map(int, input().split())
    w = list(map(int, input().split()))
    
    heap = [-x for x in w]
    heapq.heapify(heap)
    
    for i in range(m):
        largest = -heapq.heappop(heap)
        
        if largest == 0:
            heapq.heappush(heap, -largest)
            break
        
        largest -= 1
        heapq.heappush(heap, -largest)
        
    result = 0
    while heap:
        x = -heapq.heappop(heap)
        result = (result + x*x) % MOD

    print(result)




if __name__ == '__main__':
    main()
