word = input()

alpha_croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

length = len(word)
cnt= 0
for croa in alpha_croa:
    if croa != 'z=':
        tmp_cnt = word.count(croa)
        length -= len(croa) * tmp_cnt
    else:
        tmp_cnt = word.count(croa)
        tmp_cnt -= word.count('dz=')
        length -= len(croa) * tmp_cnt
        
    cnt += tmp_cnt

cnt += length
print(cnt)