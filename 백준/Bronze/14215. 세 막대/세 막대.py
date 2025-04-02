bars = list(map(int, input().split()))

if max(bars) >= (sum(bars)-max(bars)):
    print((sum(bars)-max(bars)) + (sum(bars)-max(bars)-1))
else:
    print(sum(bars))