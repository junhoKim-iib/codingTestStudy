import sys

input = sys.stdin.readline

N, L = map(int, input().split())
spot_list = sorted(list(map(int, input().split())))

answer = 0
cur_fixed = 0
for spot in spot_list:
    if spot + 0.5 > cur_fixed:
        answer += 1
        cur_fixed = spot + L - 0.5

    else:
        continue

print(answer)



