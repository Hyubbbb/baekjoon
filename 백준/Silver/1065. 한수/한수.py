import sys
n = int(sys.stdin.readline())

cnt = 0
for i in range(1, n+1):
    num_len = len(str(i))
    num_list = list(str(i))
    
    if num_len <= 2:
       cnt += 1 
    
    else:
        if int(num_list[1]) - int(num_list[0]) == int(num_list[2]) - int(num_list[1]):
            cnt += 1
        else:
            cnt += 0

print(cnt)