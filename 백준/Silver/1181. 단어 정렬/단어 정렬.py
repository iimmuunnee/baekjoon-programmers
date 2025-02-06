import sys

n = int(sys.stdin.readline())

word_list = list(set([sys.stdin.readline().strip() for i in range(n)]))

word_list.sort(key=lambda x: (len(x) ,x))

for w in word_list:
    sys.stdout.write(w + "\n")