n = int(input())
cnt = 0

for _ in range(n):
    word = input()
    is_group = True
    seen = set()
    prev = ''

    for char in word:
        if char != prev:
            if char in seen:
                is_group = False
                break
            seen.add(char)
        prev = char
    
    if is_group:
        cnt += 1

print(cnt)
