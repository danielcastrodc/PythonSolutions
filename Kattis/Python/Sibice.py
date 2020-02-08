import sys

arr = sys.stdin.readline().split()
n = int(arr[0])
w = int(arr[1])
h = int(arr[2])
d = (w**2 + h**2)**(1/2)
i = 0

while i < n:
    if int(sys.stdin.readline()) <= d:
        print("DA")
    else:
        print("NE")
    i += 1
