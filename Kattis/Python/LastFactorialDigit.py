import sys

n = int(sys.stdin.readline())
i = 0
def factorial(n):
    return 1 if (n==1 or n==0) else factorial(n-1) * n

while i < n:
    line = int(sys.stdin.readline())
    val = factorial(line)
    s = str(val)[len(str(val))-1]
    print(s)
    i += 1
