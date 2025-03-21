import sys, heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    prompt = int(sys.stdin.readline())
    
    if prompt == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-prompt, prompt))