import sys

input = sys.stdin.readline

def solution():
    s = input().strip()
    boom_string = input().strip()

    boom_len = len(boom_string)
    last_clear = boom_string[-1] # 4
    stack = []

    for char in s:
        stack.append(char)

        # 현재 넣은 글자가 폭발 문자열의 마지막과 같다면?
        # 스택에 있는 글자가 폭발 문자열보다 크거나 같아야만 가능성이 있음
        if char == last_clear and len(stack) >= boom_len:
            # 폭발 문자열 길이만큼 스택 뒷부분을 떼어봤을 때 같다면 폭발
            if stack[-boom_len:] == list(boom_string):
                del stack[-boom_len:]
    
    if stack:
        print("".join(stack))
    else:
        print("FRULA")

if __name__ == "__main__":
    solution()