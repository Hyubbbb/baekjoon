import sys
input = sys.stdin.readline

while True:
    length = sorted(list(map(int, input().split())), reverse=False)
    if length[0] == length[1] == length[2] == 0:
        break
    
    a, b, c = length[0], length[1], length[2]
    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')