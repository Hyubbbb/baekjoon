import sys
n = sorted(list(map(int, input())), reverse=True)

sys.stdout.write(''.join(map(str, n)))