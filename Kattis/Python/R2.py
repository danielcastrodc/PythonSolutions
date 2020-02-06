import sys
 
for line in sys.stdin:
    n1, n2 = (int(s) for s in line.split())
    print(n2*2-n1)
