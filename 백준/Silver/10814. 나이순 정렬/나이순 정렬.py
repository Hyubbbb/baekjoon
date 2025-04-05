import sys
input = sys.stdin.readline

n = int(input())

# 1. 나이순
# 2. 가입순
mems = []
for i in range(n):
    mem = input().split()
    mems.append([int(mem[0]), i, mem[1]])

mems = sorted(mems)

# 출력
for mem in mems:
    print(mem[0], mem[2])