import sys
input = sys.stdin.readline

while True:
    full = input().rstrip()
    if full == '#':
        break
    
    alpha = full[0]
    sentence = full[2:].lower()
    
    print(f'{alpha} {sentence.count(alpha)}')