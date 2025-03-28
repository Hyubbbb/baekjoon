n = int(input())

line = 1
while n-line > 0:
    n -= line
    line += 1

total = line+1
if line%2==0: # 짝수
    print(f'{n}/{total-n}')
else: # 홀수
    print(f'{total-n}/{n}')