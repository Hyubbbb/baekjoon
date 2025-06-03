import sys
input = sys.stdin.readline

N = int(input())

tree = {}
# 트리 입력받기
for _ in range(N):
    parent, left, right = input().split()
    tree[parent] = (left, right)

# 전위 순회: 부모 -> 좌 -> 우
def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node][0]) # 왼쪽 자식
    preorder(tree[node][1]) # 오른쪽 자식

# 중위 순회: 좌 -> 부모 -> 우
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0]) # 왼쪽 자식
    print(node, end='')
    inorder(tree[node][1]) # 오른쪽 자식

# 후위 순회: 좌 -> 우 -> 부모 
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0]) # 왼쪽 자식
    postorder(tree[node][1]) # 오른쪽 자식
    print(node, end='')

# 출력
preorder('A')
print()
inorder('A')
print()
postorder('A')