import sys
input = sys.stdin.readline

T = int(input()) # Test Case

for _ in range(T):
    N = int(input())
    dict_species = {}
    for _ in range(N):
        name, species = input().split()
        dict_species[species] = dict_species.get(species, 0) + 1 # key가 존재하면 + 1, 존재하지 않으면 1을 할당
    
    # 경우의 수 계산: 각 `species+1`을 곱하고, 마지막에 -1 (홀딱 벗은 경우의 수가 포함되니까)
    result = 1
    for i in dict_species.values():
        result *= i+1
    
    result-=1 # 홀딱 벗은 거 제외
    print(result)