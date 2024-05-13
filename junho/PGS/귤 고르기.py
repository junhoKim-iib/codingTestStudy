def solution(k, tangerine):
    answer = 0
    
    cnt_list = [0 for i in range(max(tangerine) + 1)]
    for i in tangerine:
        cnt_list[i] += 1
    
    cnt_list = sorted(cnt_list, reverse=True)
    
    total = 0
    
    for val in cnt_list:
        if total >= k:
            return answer
        else:
            total += val 
            answer += 1
    
    return answer