import sys

input = sys.stdin.readline

n = int(input())

def get_sum(n):
    sum_list = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            sum_list[j] += i
    return sum(sum_list)


print(get_sum(n))