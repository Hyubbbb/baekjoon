n = int(input())

"""
1 3 1
1 3 1
full
1 3 1
full
"""

# 1. 윗쪽
for r in range(2*n):
    print('@'*n, end='')
    print(' '*(3*n), end='')
    print('@'*n)

# 2. 가운데 풀
for r in range(n):
    print('@'*(5*n))
    
# 3. 중간
for r in range(n):
    print('@'*n, end='')
    print(' '*(3*n), end='')
    print('@'*n)

# 4. 아래 풀
for r in range(n):
    print('@'*(5*n))
