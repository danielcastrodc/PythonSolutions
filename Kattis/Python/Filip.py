import sys

n1, n2 = (int(s) for s in sys.stdin.readline().split())
s1 = str(n1)[::-1]
s2 = str(n2)[::-1]
print(int(s1) if int(s1) > int(s2) else int(s2))
