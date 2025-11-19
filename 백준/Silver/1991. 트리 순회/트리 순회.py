import sys

input = sys.stdin.readline
# A가 항상 루트노드
n = int(input())
left = [-1] * n
right = [-1] * n

for i in range(n):
    p, l, r = input().split()
    pi = ord(p) - ord('A')
    if l != '.':
        left[pi] = ord(l) - ord('A')
    if r != '.':
        right[pi] = ord(r) - ord('A')

def preorder(x):
    if x == -1:
        return
    print(chr(x + ord('A')), end="")
    preorder(left[x])
    preorder(right[x])

def inorder(x):
    if x == -1:
        return
    inorder(left[x])
    print(chr(x + ord('A')), end="")
    inorder(right[x])

def postorder(x):
    if x == -1:
        return
    postorder(left[x])
    postorder(right[x])
    print(chr(x + ord('A')), end="")

preorder(0)
print()
inorder(0)
print()
postorder(0)