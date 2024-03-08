def solution(s, skip, index):
    answer = ''
    w_list = [chr(w) for w in range(97,123) if chr(w) not in skip]
    
    for w in s:
        answer += w_list[(w_list.index(w) + index) % len(w_list)]
    
    return answer