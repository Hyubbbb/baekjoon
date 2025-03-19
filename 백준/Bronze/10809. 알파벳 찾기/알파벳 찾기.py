s = input()

for i in range(97, 123):
    try:
        print(s.index(chr(i)), end=' ')
    except:
        print(-1, end=' ')