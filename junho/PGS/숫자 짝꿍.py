def solution(X, Y):
    answer = ''
    X_cnt_list = [0] * 10
    Y_cnt_list = [0] * 10
    
    for ch in X:
        X_cnt_list[int(ch)] += 1
    
    for ch in Y:
        Y_cnt_list[int(ch)] += 1
    
    for i in range(len(X_cnt_list) - 1,-1,-1):
        answer += str(i) * min(X_cnt_list[i], Y_cnt_list[i])
    
    if answer == "":
        answer = "-1"

    elif answer[0] == "0":
        answer = "0"
        
    return answer 