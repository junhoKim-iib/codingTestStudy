import sys 


def dfs(n):
    if not visited[n]:
        visited[n] = 1
    
    for i in adj_list[n]:
        if not visited[i]:
            dfs(i)


input = sys.stdin.readline

n, m = map(int, input().split())

visited = [0 for _ in range(n)]
adj_list = [[] for i in range(n)]

cnt = 0

for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u - 1].append(v -1)
    adj_list[v - 1].append(u -1)


for i in range(n):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)