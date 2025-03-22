n = int(input())

for i in range(1, 2*n):
    if i <= n:
        num_1 = n - i
        num_2 = 2*i - 1
        # print(i)
        print(' '*num_1, '*'*num_2, sep='')
    else:
        num_1 = i-n
        num_2 = 2*(n-(i-n)) -1
        # print(i-n)
        print(' '*num_1, '*'*num_2, sep='')