def solve(n, k):
    import heapq

    heap = [(-n, 1)]
    total = 0

    while True:
        length, count = heapq.heappop(heap)
        length = -length
        left = (length - 1) // 2
        right = length // 2

        if total + count >= k + 1:
            print(min(left, right), max(left, right))
            return

        total += count
        heapq.heappush(heap, (-left, count))
        heapq.heappush(heap, (-right, count))

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    n, k = map(int, input().split())
    solve(n, k)
