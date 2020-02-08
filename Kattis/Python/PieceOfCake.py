import sys

n1, n2, n3 = (int(s) for s in sys.stdin.readline().split())
total = max(n1-n2,n2) * max(n1-n3,n3) * 4
print(total)
