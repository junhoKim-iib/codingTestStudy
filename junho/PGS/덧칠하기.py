def solution(n, m, section):
    
    cur_idx = 0
    answer = 0
    
    while section:
        cur_idx = section[0] + m
        answer += 1
        i = 1
        while i < len(section) and section[i] < cur_idx:
            i += 1
        section = section[i:]

    return answer