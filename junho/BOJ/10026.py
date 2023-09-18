import sys
import collections
sys.setrecursionlimit(100000)
import math

x = [0,0,1,-1]
y = [1,-1,0,0]


total = 0
blind = 0

def bfs(arr, i, j, color):
    n = len(arr)
    queue =  collections.deque()
    queue.append((i,j))
    arr[i][j] = '0'
    
    while queue:
        cur_x , cur_y = queue.popleft()
        for i in range(4):
            nx = cur_x + x[i]
            ny = cur_y + y[i]
            if nx < 0 or nx >= n or ny < 0 or ny>= n:
                continue
            if arr[nx][ny] == color:
                arr[nx][ny] = '0'
                queue.append((nx,ny))
    


n = int(sys.stdin.readline().strip())

arr = []
arr2 = []
for _ in range(n):
    line = sys.stdin.readline()
    line2 = line.replace("G", "R")

    line = list(map(str,line.strip()))
    line2 = list(map(str, line2.strip()))
    arr.append(line)
    arr2.append(line2)
    

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            total += 1
            bfs(arr,i,j,'R')

        if arr[i][j] == 'G':
            total += 1
            bfs(arr,i,j,'G')

        if arr[i][j] == 'B':
            total += 1
            bfs(arr,i,j,'B')



for i in range(n):
    for j in range(n):
        if arr2[i][j] == 'R':
            blind += 1
            bfs(arr2,i,j,'R')

        if arr2[i][j] == 'B':
            blind += 1
            bfs(arr2,i,j,'B')


print(total, blind)