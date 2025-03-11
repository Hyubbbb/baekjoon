import sys

while True:
    
    x = int(sys.stdin.readline())
    
    if x == 0:
     break

    cnt = int(x*(x+1)/2)
    print(cnt)