n = int(input())

if n%2==0: # 짝수인 경우
    print('I LOVE CBNU')
else:
    print('*'*n)
    print(' '*((n-1)//2) + '*')
    for i in range(1, (n-1)//2 + 1):
        print(' '*((n-2*i-1)//2) + '*' + ' '*(2*i -1) + '*')