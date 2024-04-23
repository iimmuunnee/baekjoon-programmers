def solution(array, n):
    array.sort()  # 배열을 정렬
    left = 0
    right = len(array) - 1
    index = binary_search(array, n, left, right)
    return array[index]

def binary_search(arr, key, left, right):
    # 배열 범위 내에서 가장 가까운 인덱스를 찾는 이진 탐색 함수
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    
    # 배열 내에서 가장 가까운 값이 없는 경우 처리
    if right < 0:
        return 0
    elif left > len(arr) - 1:
        return len(arr) - 1
    else:
        # 주어진 키와 가장 가까운 값이 있는 인덱스 반환
        if abs(arr[left] - key) < abs(arr[right] - key):
            return left
        elif abs(arr[left] - key) > abs(arr[right] - key):
            return right
        else:
            return min(left, right)