import sys

def find_missing_digit(isbn):
    idx = isbn.index("*")

    for d in range(10):
        total = 0
        for i in range(13):
            if i == idx:
                val = d
            else:
                val = int(isbn[i])
            weight = 1 if i % 2 == 0 else 3
            total += weight * val

        if total % 10 == 0:
            return d
    return -1

input = sys.stdin.readline

isbn = input()

print(find_missing_digit(isbn))
