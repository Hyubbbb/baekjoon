import sys

input = sys.stdin.readline

while True:
    word = input().rstrip()
    
    # 중지 조건
    if word == '0':
        break
    
    # 문자열 길이 절반만 순회
    is_felin = True
    for i in range(len(word)//2):
        if word[i] != word[-(i+1)]:
            print('no')
            is_felin = False
            break
    if is_felin:
        print('yes')