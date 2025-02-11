import sys

input = sys.stdin.readline

def stack_sequence():
    n = int(input())

    target = [int(input()) for _ in range(n)]
    result = []
    next_num = 1
    answer = []
    for t in target:
        while True:
            if not result or t != result[-1]:
                if n >= next_num:
                    result.append(next_num)
                    next_num += 1
                    answer.append("+")
                else:
                    return ["NO"]
            else:
                result.pop()
                answer.append("-")
                break
    return answer



sys.stdout.write("\n".join(stack_sequence()))