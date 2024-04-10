def solution(bandage, health, attacks):
    answer = health
    prev_time = 0 
    
    for atk in attacks:
        cal_time = atk[0] - prev_time - 1
        if answer < health and cal_time >= 1:
            answer += (cal_time * bandage[1]) + ((cal_time // bandage[0]) * bandage[2])
            if answer > health:
                answer = health 
        
        answer -= atk[1] 
        prev_time = atk[0]
        
        if answer <= 0:
            return -1
        
    return answer