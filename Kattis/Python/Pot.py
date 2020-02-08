import sys

n = int(sys.stdin.readline())
i = 0
total = 0

while i < n:
    ini = sys.stdin.readline()
    n1 = ini[0:len(ini)-2]
    n2 = ini[len(ini)-2]
    total += int(n1) ** int(n2)
    i += 1
print(total)
