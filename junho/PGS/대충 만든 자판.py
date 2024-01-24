def solution(keymap, targets):
    answer = []
    ch_dict = {}
    find = 0

    for target in targets:
        cnt = 0
        
        for ch in target:
            if ch in ch_dict:
                cnt += ch_dict[ch]
                
            else:
                for i in range(100):
                    for key in keymap:
                        try:
                            if key[i] == ch:
                                ch_dict[ch] = i+1
                                cnt += ch_dict[ch]
                                find = 1
                                break
                        except:
                            continue
                            
                    if find == 1:
                        break
                        
                if find == 0:
                    cnt = -1
                    break
                    
                else:
                    find = 0
                    
        answer.append(cnt)
                
    return answer