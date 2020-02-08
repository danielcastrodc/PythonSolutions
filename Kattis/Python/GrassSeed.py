import sys

cost = float(sys.stdin.readline())
n = int(sys.stdin.readline())
i = 0
total = 0.0

while i < n:
    n1, n2 = (float(s) for s in sys.stdin.readline().split())
    total += n1 * n2 * cost
    i += 1
print("{0:.8f}".format(total))
