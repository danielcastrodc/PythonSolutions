import sys

n1, n2, n3 = (int(s) for s in sys.stdin.readline().split())
i = 1
n3 += 1

while i < n3:
    if i%n1==0 and i%n2==0:
        print("FizzBuzz")
    elif i%n1==0 and i%n2!=0:
        print("Fizz")
    elif i%n1!=0 and i%n2==0:
        print("Buzz")
    else:
        print(str(i))
    i += 1
