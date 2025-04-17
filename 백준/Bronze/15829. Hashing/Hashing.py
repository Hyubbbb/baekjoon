import sys
input = sys.stdin.readline

l = int(input())
word = input().rstrip()

def hashing(l, word):
    r = 31
    m = 1234567891
    
    result = 0
    for i in range(l):
        result += (ord(word[i])-96) * r**i
    
    return result

print(hashing(l, word))