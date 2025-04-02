import sys

while True:
    lengths = list(map(int, sys.stdin.readline().split()))
    if lengths == [0, 0, 0]:
        break
    
    if max(lengths) >= (sum(lengths)-max(lengths)):
        print('Invalid')
    elif lengths[0]==lengths[1]==lengths[2]:
        print('Equilateral')
    elif lengths[0]==lengths[1] or lengths[1]==lengths[2] or lengths[0]==lengths[2]:
        print('Isosceles')
    else:
        print('Scalene')