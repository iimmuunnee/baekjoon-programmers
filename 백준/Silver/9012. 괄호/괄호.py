import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    sentence = input().rstrip()

    if sentence == ".":
        break

    stack = []
    is_balanced = True

    for char in sentence:
        if char in "(":
            stack.append(char)
        elif char == ")":
            if stack and stack[-1] == "(": # stack이 비어있지않고 가장 뒷 괄호가 같은 종류의 여는 괄호인지
                stack.pop() # 완벽하게 된 괄호는 삭제
            else:
                is_balanced = False
                break
      
    if is_balanced and not stack:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")