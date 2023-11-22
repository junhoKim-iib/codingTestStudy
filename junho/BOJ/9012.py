import sys

for _ in range(int(sys.stdin.readline())):
    cnt = 0

    for ch in sys.stdin.readline().strip():
        if ch == '(':
            cnt += 1
        else:
            if cnt <= 0:
                cnt -= 1
                break
            cnt -= 1

    print("YES" if cnt==0 else "NO")