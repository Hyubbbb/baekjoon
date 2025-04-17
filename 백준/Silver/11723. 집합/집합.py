import sys
input = sys.stdin.readline

n = int(input())


s = set()
for _ in range(n):
    prompt = input().split()
    
    p = prompt[0]
    if p == 'add':
        s.add(int(prompt[1]))
    elif p == 'remove' and int(prompt[1]) in s:
        s.remove(int(prompt[1]))
    elif p == 'check':
        if int(prompt[1]) in s:
            print(1)
        else:
            print(0)
    elif p == 'toggle':
        if int(prompt[1]) in s:
            s.remove(int(prompt[1]))
        else:
            s.add(int(prompt[1]))
    elif p == 'all':
        s = set(range(1, 21))
    elif p == 'empty':
        s = set()