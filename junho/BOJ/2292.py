import sys
input = sys.stdin.readline

N = int(input())
cnt = 1
mul_num = 6
res = 1

while True:
    if N <= res:
        print(cnt)
        break
    
    res += mul_num
    mul_num += 6
    cnt += 1
