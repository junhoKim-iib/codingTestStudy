import sys
from collections import deque
input = sys.stdin.readline

n = int(input())


deck = deque()

for _ in range(n):
    com = list(map(int, input().split()))

    if com[0] == 1:
        deck.appendleft(com[1])
    
    elif com[0] == 2:
        deck.append(com[1])

    elif com[0] == 3:
        if len(deck):
            print(deck.popleft())
        else:
            print(-1)

    elif com[0] == 4:
        if len(deck):
            print(deck.pop())
        else:
            print(-1)


    elif com[0] == 5:
        print(len(deck))

    elif com[0] == 6:
        if len(deck):
            print(0)
        else:
            print(1)

    elif com[0] == 7:
        if len(deck):
            print(deck[0])
        else:
            print(-1)        

    elif com[0] == 8:
        if len(deck):
            print(deck[len(deck) - 1])
        
        else:
            print(-1)
