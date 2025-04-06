import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# n개 줄: 포켓몬 이름
pokemons = ['empty']
_dict = {}
for i in range(n):
    name = input().rstrip()
    pokemons.append(name)
    _dict[name] = i+1

# m개 줄: 맞혀야 하는 문제
for _ in range(m):
    question = input().rstrip()
    try:
        print(pokemons[int(question)])
    except:
        print(_dict[question])
    
# 리스트를 쓰면 시간 초과할 거 같아