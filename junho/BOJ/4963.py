import sys

input = sys.stdin.readline


def dfs(x,y):

    if x < 0 or y < 0 or x >= m or y >= n or mat[x][y] == 0:
        return 

    mat[x][y] = 0

    dfs(x + 1,y)
    dfs(x - 1,y)
    dfs(x,y + 1)
    dfs(x,y - 1)

    dfs(x + 1,y + 1)
    dfs(x + 1,y - 1)
    dfs(x - 1,y - 1)
    dfs(x - 1,y + 1)
    

global n, m
n, m = map(int, input().split())

while n and m:
    mat = []
    cnt = 0
    for _ in range(m):
        mat.append(list(map(int, input().split())))

    for i in range(m):
        for j in range(n):
            if mat[i][j]:
                cnt += 1
                dfs(i,j)

    print(cnt)    

    n, m = map(int, input().split())