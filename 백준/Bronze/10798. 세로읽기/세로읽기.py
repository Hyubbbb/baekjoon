import sys

lines = sys.stdin.read().splitlines()

max_len = max(map(len, lines))


word = ''

for i in range(max_len):
    for j in range(len(lines)):
        try:
            word += lines[j][i]
        except:
            continue

print(word)