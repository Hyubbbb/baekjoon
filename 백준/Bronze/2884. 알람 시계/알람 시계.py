import sys

h, m = map(int, sys.stdin.readline().split(' '))

m_new = m - 45
if m_new >= 0:
    print(h, m_new)
else:
    m_new = m + 15
    h_new = h - 1
    if h_new < 0:
        h_new = 23
    
    print(h_new, m_new)