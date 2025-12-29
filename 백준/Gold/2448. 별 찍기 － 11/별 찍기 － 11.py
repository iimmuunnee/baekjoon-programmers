import sys

input = sys.stdin.readline

def solution():
    stars = ["  *  ", " * * ", "*****"]
    N = int(input())

    current_size = 3

    while current_size < N:
        new_stars = []

        for s in stars:
            new_stars.append(" " * (current_size) + s + " " * (current_size))
        for s in stars:
            new_stars.append(s + " " + s) 
        
        stars = new_stars
        current_size *= 2

    for s in stars:
        print(s)

if __name__ == "__main__":
    solution()