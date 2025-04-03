import sys

n, m = map(int, input().split())

board = sys.stdin.read().splitlines()

min_count = 64
for i in range(n-7):
    for j in range(m-7):
        count1 = 0
        count2 = 0
        
        for x in range(i, i+8):
            for y in range(j, j+8):
                now = board[x][y]
                
                if (x+y)%2 == 0:
                    count1 += (now != 'W') # W로 시작한다고 기대
                    count2 += (now != 'B')
                else:
                    count1 += (now != 'B') # W로 시작한다고 기대
                    count2 += (now != 'W')
                    
        min_count = min(min_count, count1, count2)

print(min_count)