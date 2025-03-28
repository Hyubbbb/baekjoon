n, b = map(int, input().split())


def to_base36(num, b):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num == 0:
        return "0"
    
    result = ""
    while num > 0:
        num, remainder = divmod(num, b)
        result = chars[remainder] + result
    return result

print(to_base36(n, b))