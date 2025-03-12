import sys

h, m = map(int, sys.stdin.readline().split(' '))
t = int(sys.stdin.readline())

m_new = m+t

if m_new < 60:
    print(h, m_new)
else:
    h_new = h + (m_new // 60)
    m_new = m_new % 60
    if h_new >= 24:
        h_new = h_new % 24
    print(h_new, m_new)