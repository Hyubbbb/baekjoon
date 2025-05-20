import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

white, blue = 0, 0

def cut(x, y, size):
    global white, blue
    color = graph[y][x] # 1이면 blue, 0이면 white
    for i in range(x, x+size):
        for j in range(y, y+size):
            if graph[j][i] != color:
                cut(x, y, size//2)
                cut(x+size//2, y, size//2)
                cut(x, y+size//2, size//2)
                cut(x+size//2, y+size//2, size//2)
                return
    if color == 1:
        blue += 1
    else:
        white += 1

# 결과 출력
cut(0, 0, N)
print(white)
print(blue)