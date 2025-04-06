import sys
input = sys.stdin.readline

n = int(input())

entered_mems = set()
for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        entered_mems.add(name)
    else:
        entered_mems.remove(name)

entered_mems = sorted(entered_mems, reverse=True)

sys.stdout.write('\n'.join(map(str, entered_mems)) + '\n')