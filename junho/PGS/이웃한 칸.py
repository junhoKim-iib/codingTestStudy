dh = [0,1,-1,0]
dw = [-1,0,0,1]

def solution(board, h, w):
    answer = 0
    
    cur_color = board[h][w]
    
    for i in range(4):
        try:
            h_check, w_check = h + dh[i], w +dw[i]
            if board[h_check][w_check] == cur_color and h_check >= 0 and w_check >=0 :
                answer += 1
        except:
            pass
    
    return answer