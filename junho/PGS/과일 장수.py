def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    
    times = len(score) // m
    idx = 0
    
    for _ in range(times):
        answer += min(score[idx: idx + m]) * m
        idx += m
        
    return answer