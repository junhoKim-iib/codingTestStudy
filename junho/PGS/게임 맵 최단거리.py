from collections import deque


def solution(maps):
    max_x = len(maps[0])
    max_y = len(maps)
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    cnt = 1
    
    q_list = deque()
    q_list.append((0,0))
    
    while q_list:
        for _ in range(len(q_list)):
            cur_y, cur_x = q_list.popleft()

            for i in range(4):
                nx = cur_x + dx[i]
                ny =  cur_y + dy[i]

                if 0 <= nx <max_x and 0 <= ny < max_y:
                    if nx == max_x - 1 and ny == max_y - 1:
                        return cnt + 1

                    elif maps[ny][nx] == 1:
                        q_list.append((ny,nx))
                        maps[ny][nx] = 0
                        
        cnt += 1

    return -1 