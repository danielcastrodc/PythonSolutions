import sys

n1 = int(sys.stdin.readline())
n2 = int(sys.stdin.readline())
if n1 < 0 and n2 < 0:
    print(3)
elif n1 > 0 and n2 < 0:
    print(4)
elif n1 > 0 and n2 > 0:
    print(1)
else:
    print(2)
