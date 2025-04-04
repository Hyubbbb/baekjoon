a, b = map(int, input().split())

if abs((a+b)/2 - int((a+b)/2)) > 0 or a+b <0 or a-b <0:
    print(-1)
else:
    print(int((a+b)/2), int((a-b)/2))