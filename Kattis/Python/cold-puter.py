import sys

i = 0
n = int(sys.stdin.readline())
arr = sys.stdin.readline().split()
total = 0
while i < n:
    if int(arr[i]) < 0:
        total = total+1
    i = i+1
    
print(total)
