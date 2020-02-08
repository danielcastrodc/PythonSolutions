import sys

arr = sys.stdin.readline().split("-")
i = 0
n = len(arr)
s = ""
while i < n:
    s += arr[i][0]
    i += 1

print(s)
    
