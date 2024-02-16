from itertools import combinations
import sys

input = sys.stdin.readline

hobbit_list = [int(input()) for _ in range(9)]

for combi in combinations(hobbit_list, 7):
    
    if sum(combi) == 100:
        for hobbit in sorted(combi):
            print(hobbit)
        break


