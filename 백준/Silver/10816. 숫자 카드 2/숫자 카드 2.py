import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split())) # 중복 있음

_dict = {}
for card in cards:
    _dict[card] = _dict.get(card, 0) + 1
        
m = int(input())
valid_cards = list(map(int, input().split())) # 중복 없음
for valid_card in valid_cards:
    print(_dict.get(valid_card, 0), end=' ')