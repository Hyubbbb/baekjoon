import sys
input = sys.stdin.readline

n = int(input())
chus = list(map(int, input().rstrip().split(' ')))
# chus = sorted(chus, reverse = True)
chus = sorted(chus, reverse = False)

def min_weight(chus):
    pos = 0
    for chu in chus:
        if pos+1 < chu:
            return(pos+1)
        else:
            pos += chu

    return pos+1

print(min_weight(chus))