import sys

val_max = -1
val_row = 0
for i in range(9):
    line = list(map(int, sys.stdin.readline().strip().split(' ')))

    line_max = max(line)
    
    if line_max > val_max:
        val_max = line_max
        val_row = i+1
        val_col = line.index(line_max) + 1


print(val_max)
print(val_row, val_col)