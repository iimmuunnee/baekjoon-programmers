import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

stack = []

for _ in range(n):
    command = input().strip().split()

    if command[0] == "push":
        stack.append(command[1])

    elif command[0] == "pop":
        if len(stack) > 0:
            print(str(stack.pop()) + "\n")
        else:
            print("-1\n")

    elif command[0] == "size":
        print(str(len(stack)) + "\n")

    elif command[0] == "empty":
        if len(stack) > 0:
            print("0\n")
        else:
            print("1\n")

    elif command[0] == "top":
        if len(stack) > 0:
            print(str(stack[-1]) + "\n")
        else:
            print("-1\n")