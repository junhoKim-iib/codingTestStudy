import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def bi_search(target:int, arr_list):
    start, end = 0, len(arr_list) -1
    while(start <= end):
        mid = (start + end) // 2
        if arr_list[mid] == target:
            return 1
        elif arr_list[mid] > target:
            end = mid - 1
        elif arr_list[mid] < target:
            start = mid + 1
    
    return 0


n = int(input())
std_list = list(map(int, input().split()))
m = int(input())
comp_list = list(map(int, input().split())) 


std_list.sort()

for val in comp_list:
    print(bi_search(val, std_list), end=' ')
