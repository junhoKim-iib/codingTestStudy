import sys

input = sys.stdin.readline

n = int(input())
n_set = set(map(int, input().split()))

print(*sorted(n_set))