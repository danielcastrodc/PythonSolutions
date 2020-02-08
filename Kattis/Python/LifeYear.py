import sys

n = int(sys.stdin.readline())
i = 0
total = 0

while i < n:
    n1, n2 = (float(s) for s in sys.stdin.readline().split())
    total += n1 * n2
    i += 1
print(total)
