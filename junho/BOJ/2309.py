from itertools import combinations
import sys

input = sys.stdin.readline

hobbit_list = []

for _ in range(9):
    hobbit_list.append(int(input()))

for i in combinations(hobbit_list, 2):
    result = [hobbit for hobbit in hobbit_list if hobbit not in i]

    if sum(result) == 100:
        for hobbit in sorted(result):
            print(hobbit)
        break


