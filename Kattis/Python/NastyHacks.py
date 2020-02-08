import sys

n = int(sys.stdin.readline())
i = 0

while i < n:
    arr = sys.stdin.readline().split()
    r = int(arr[0])
    e = int(arr[1])
    c = int(arr[2])
    d = e-c
    if r < d:
        print("advertise")
    elif r == d:
        print("does not matter")
    else:
        print("do not advertise")
    i += 1
