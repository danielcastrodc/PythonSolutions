import sys

arr = sys.stdin.readline().split()
comp = [1,1,2,2,2,8]
i = 0
n = 6
s = ""
while i < n:
    s += str(comp[i] - int(arr[i])) + " "
    i += 1

print(s)
    
