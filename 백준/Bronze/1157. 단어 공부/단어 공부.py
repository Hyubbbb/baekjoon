words = input().lower()

dict = {}
for word in words:
    try:
        dict[word] += 1
    except: 
        dict[word] = 1

max_val = max(dict.values())
max_list = [k for k, v in dict.items() if v == max_val]

if len(max_list) == 1:
    print(max_list[0].upper())
else:
    print('?')