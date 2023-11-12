import sys

T = int(sys.stdin.readline())

for _ in range(T):
    cnt = 0
    ps = sys.stdin.readline().strip()

    for ch in ps:
        if ch == '(':
            cnt += 1
        else:
            if cnt <= 0:
                cnt -= 1
                break
            cnt -= 1

            
    if cnt == 0:
        print('YES')
    else: 
        print("NO")