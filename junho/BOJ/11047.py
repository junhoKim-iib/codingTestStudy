import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

answer = 0

for i in range(len(arr) - 1, -1, -1):
    cnt = K // arr[i]
    answer += cnt
    K -= cnt * arr[i]

print(answer)