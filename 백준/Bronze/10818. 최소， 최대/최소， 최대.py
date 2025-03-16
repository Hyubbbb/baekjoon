import sys

n = int(input())

a = input().split(' ')

int_a = [int(i) for i in a]

print(min(int_a), max(int_a))