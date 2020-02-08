import sys

time = sys.stdin.readline().split()
base = [24, 60]
if int(time[1]) - 45 < 0:
    if int(time[0])-1 == -1:
        print("23 " + str(60+int(time[1])-45))
    else:
        print(str(int(time[0])-1) + " " + str(60+int(time[1])-45))
else:
    print(str(int(time[0])) + " " + str(int(time[1])-45))

    
