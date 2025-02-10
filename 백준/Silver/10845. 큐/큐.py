import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

queue = deque()

for _ in range(n):
    command = input().rstrip().split()

    if command[0] == "push":
        queue.append(command[1])
    
    elif command[0] == "pop":
        print(str(queue.popleft()) + "\n" if queue else "-1\n")

    elif command[0] == "size":
        print(str(len(queue)) + "\n")
    
    elif command[0] == "empty":
        print("0\n" if queue else "1\n") # 비어있으면 1
    
    elif command[0] == "front":
        print(f"{queue[0]}\n" if queue else "-1\n") # 비어있으면 -1
    
    elif command[0] == "back":
        print(f"{queue[-1]}\n" if queue else "-1\n") # 비어있으면 -1