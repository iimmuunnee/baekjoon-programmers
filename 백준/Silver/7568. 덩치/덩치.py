n = int(input())
answer = []
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    
for idx1, value1 in enumerate(arr):
    count = 1
    for idx2, value2 in enumerate(arr):
        if idx1 != idx2:
            if value1[0] < value2[0] and value1[1] < value2[1]:
                count += 1
    answer.append(count)
print(" ".join(map(str, answer)))
