def to_base_n(num, base):
    digits = '0123456789ABCDEF'
    result = ''
    while num > 0:
        result = digits[num % base] + result
        num //= base
    return result or '0'

def is_palindrome(s):
    return s == s[::-1]

T = int(input())
for _ in range(T):
    A, n = map(int, input().split())
    converted = to_base_n(A, n)
    print(1 if is_palindrome(converted) else 0)