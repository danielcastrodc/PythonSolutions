import sys

mb = int(sys.stdin.readline())
n = int(sys.stdin.readline())
i = 0
total = 0
while i < n:
    line = int(sys.stdin.readline())
    total += mb - line
    i += 1

print(total + mb)
    
