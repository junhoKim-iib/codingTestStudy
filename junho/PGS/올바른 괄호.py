def solution(s):
    answer = True
    
    
    ans_list = []
    for ch in s:
        if ch == '(':
            ans_list.append(ch)
        else:
            try:
                ans_list.pop()
            except:
                return False
    
    if len(ans_list) == 0:
        return True
    else:
        return False