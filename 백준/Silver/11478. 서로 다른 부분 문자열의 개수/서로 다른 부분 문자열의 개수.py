import sys
words = sys.stdin.readline().rstrip()
length = len(words)

_list = []
for i in range(length+1):
    for j in range(i+1, length+1):
        _list.append(words[i:j])
        # print(f'i = {i}\nj = {j}\n{_list}')

# print(set(_list))
print(len(set(_list)))