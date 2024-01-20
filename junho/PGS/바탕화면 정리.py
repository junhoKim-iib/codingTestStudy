def solution(wallpaper):
    answer = [-1,-1,-1,-1]
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if  answer[0] == -1 or answer[0] > i:
                    answer[0] = i
                
                if answer[1] == -1 or answer[1] > j:
                    answer[1] = j
                
                if answer[2] == -1 or answer[2] < i:
                    answer[2] = i
                
                if answer[3] == -1 or answer[3] < j:
                    answer[3] = j
                    
    answer[2] += 1
    answer[3] += 1
                
    return answer