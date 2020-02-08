import sys

n = int(sys.stdin.readline())
i = 0
while i < n:
    val = int(sys.stdin.readline())
    if val % 2 == 0:
        print(str(val) + " is even")
    else:
        print(str(val) + " is odd")
    i += 1
