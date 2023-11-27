import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []


for _ in range(N):
    x = int(input())
    if x > 0:
        # push to the heap
        heapq.heappush(heap, x)
        
    elif x == 0:
        # print the min value and delete it from the heap
        try:
            print(heapq.heappop(heap))
        
        except:
            print(0)

    