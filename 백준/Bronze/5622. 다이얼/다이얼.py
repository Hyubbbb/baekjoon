word = input()

time = 0

for i in word:
    if 65 <= ord(i) <= 67:
        time += 3
    elif ord(i) <= 70:
        time += 4
    elif ord(i) <= 73:
        time += 5
    elif ord(i) <= 76:
        time += 6
    elif ord(i) <= 79:
        time += 7
    elif ord(i) <= 83:
        time += 8
    elif ord(i) <= 86:
        time += 9
    elif ord(i) <= 90:
        time += 10
print(time)