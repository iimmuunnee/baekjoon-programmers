import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# 왼쪽 서브트리의 모든 값 < 루트 < 오른쪽 서브트리 값
# 전위 순회(루트, 왼쪽, 오른쪽)한 결과를 입력받고 
# 후위 순회(왼쪽, 오른쪽, 루트)한 결과를 출력하라.

# 전위 순회 -> 첫번째 입력이 무조건 루트, 그 다음 루트보다 작은 값, 루트보다 큰 값들

def post_order(start, end):
    if start > end:
        return
    
    # 시작 인덱스가 항상 root -> 출력
    root = nums[start]

    idx = start + 1 # 루트보다 커지는 지점을 찾아서 오른쪽 서브트리 시작을 찾기

    while idx <= end:
        if nums[idx] > root:
            break
        idx += 1
    
    post_order(start + 1, idx - 1) # 왼쪽 서브트리 이어서 탐색
    post_order(idx, end) # 왼쪽다음인 오른쪽 서브트리 탐색
    print(root)

nums = []

while True:
    try:
        line = input()
        if not line:
            break
        nums.append(int(line))
    except:
        break

post_order(0, len(nums) - 1)

