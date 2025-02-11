import sys

input = sys.stdin.readline
write = sys.stdout.write

set_result = set([])

n = int(input())


for _ in range(n):
    command = list(input().rstrip().split(" "))
    if command[0] == 'add':
        set_result.add(int(command[1]))

    elif command[0] == "remove":
        set_result.discard(int(command[1]))

    elif command[0] == "check":
        if int(command[1]) in set_result:
            write("1\n")
        else:
            write("0\n")

    elif command[0] == "toggle":
        if int(command[1]) in set_result:
            set_result.remove(int(command[1]))
        else:
            set_result.add(int(command[1]))

    elif command[0] == "all":
        set_result = set(range(1, 21))

    elif command[0] == "empty":
        set_result = set()
    

