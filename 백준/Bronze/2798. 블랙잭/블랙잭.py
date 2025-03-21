n, m = map(int, input().split(' '))

vals = list(map(int, input().split(' ')))
vals = sorted(vals)


scores = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            score = vals[i]+vals[j]+vals[k]
            if score <= m:
                scores.append(score)
            else:
                break
print(max(scores))