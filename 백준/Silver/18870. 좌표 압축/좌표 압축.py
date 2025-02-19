import sys
import bisect

input = sys.stdin.readline

def coordinate_compression(arr):
    sorted_unique = sorted(set(arr))
    result = [str(bisect.bisect_left(sorted_unique, x)) for x in arr]

    return result

n = int(input()) # 좌표 개수

n_list = list(map(int, input().rstrip().split()))

print(" ".join(coordinate_compression(n_list)))