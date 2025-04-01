t1, t2 = map(int, input().split())

if t2 == (t1%30)*12:
    print('O')
else:
    print('X')