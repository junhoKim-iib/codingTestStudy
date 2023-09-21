import sys

input = sys.stdin.readline

N = int(input())
s = []
for _ in range(N):

    com = list(map(int,input().split()))

    if com[0] == 1:
        s.append(com[1])

    elif com[0] == 2:
        if len(s) > 0:
            print(s.pop())

        else:
            print(-1)

    elif com[0] == 3:
        print(len(s))

    elif com[0] == 4:
        if len(s) == 0:
            print(1) 
        
        else:
            print(0)

    elif com[0] == 5:
        if len(s) > 0:
            print(s[len(s) - 1])
        
        else:
            print(-1)
