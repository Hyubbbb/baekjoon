expr = input()

parts = expr.split('-')

# 1) 첫 번째 숫자가 양수인 경우
if parts[0]:
    total = sum(map(int, parts[0].split('+'))) 
    
    # 그 이후 처리
    for part in parts[1:]:
        total -= sum(map(int, part.split('+')))
    
# 2) 첫 번째 숫자가 음수인 경우
else:
    total = -1 * sum(map(int, parts[1].split('+'))) 
    
    # 그 이후 처리
    for part in parts[2:]:
        total -= sum(map(int, part.split('+')))

print(total)