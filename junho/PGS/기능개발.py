from collections import deque
 
def solution(progresses, speeds):
    answer = []
    progresses = deque((-x, index) for index, x in enumerate(progresses))
    
    while progresses:
        cnt = 0
        
        progresses = deque((x - speeds[index], index) for x, index in progresses)
        while progresses and progresses[0][0] <= -100:
            cnt += 1
            progresses.popleft()
            
        if cnt > 0:
            answer.append(cnt)
        

    return answer

