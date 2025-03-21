def d(n):
    d_n = n + sum(map(int, str(n)))
    return d_n

s_full = set(range(1, 10001))

s_not_self = set()
for i in range(1, 10001):
    if d(i) > 10000:
        pass
    s_not_self.add(d(i))

l_self = sorted(list(s_full - s_not_self))
print(*l_self, sep='\n')