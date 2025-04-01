import sys

n = int(input())

rick_list = [
    'Never gonna give you up',
    'Never gonna let you down',
    'Never gonna run around and desert you',
    'Never gonna make you cry',
    'Never gonna say goodbye',
    'Never gonna tell a lie and hurt you',
    'Never gonna stop',
    ]

is_hack = False
for _ in range(n):
    sentence = sys.stdin.readline().strip()
    if sentence in rick_list:
        continue
    else:
        is_hack = True
        break

if is_hack:
    print('Yes')
else:
    print('No')