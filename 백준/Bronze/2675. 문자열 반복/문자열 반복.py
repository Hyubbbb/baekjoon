import sys

t = int(sys.stdin.readline())

for _ in range(t):
    r, s = sys.stdin.readline().split(' ')
    s = s.strip()
    
    for i in range(len(s)):
        print(s[i]*int(r), end='')
    print()