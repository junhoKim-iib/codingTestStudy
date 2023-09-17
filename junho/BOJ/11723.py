import sys

input = sys.stdin.readline
n = int(input())

res_set = set()

for _ in range(n):
    command = input().split()

    if command[0] == "add":
        res_set.add(int(command[1]))

    elif command[0] == "remove":
        if int(command[1]) in res_set:
            res_set.discard(int(command[1]))

    elif command[0] == "check":
        if int(command[1]) in res_set:
            print(1)
        else:
            print(0)

    elif command[0] == "toggle":
        if int(command[1]) in res_set:
            res_set.discard(int(command[1]))
        else:
            res_set.add(int(command[1]))

    elif command[0] == "all":
        res_set = set([i for i in range(1,21)])

    elif command[0] == "empty":
        res_set = set()
