def solution(park, routes):
    
    cur_loc = None
    fail = 0
    
    H = len(park)
    W = len(park[0])
    
    # find start point
    for i,row in enumerate(park):
        if "S" in row:
            cur_loc = [i, row.index("S")]
            break
    
    # move
    for move in routes:
        op, n = move[0], int(move[2])
        
        if op == "N":
            if cur_loc[0] - n < 0:
                continue
            
            next_loc = cur_loc.copy()
            
            for _ in range(n):
                next_loc[0] -= 1
                
                if park[next_loc[0]][ next_loc[1]] == "X":
                    fail = 1
                    break
            
            
            if not fail:
                cur_loc = next_loc.copy()
            fail = 0
            
            
        elif op == "S":
            if cur_loc[0] + n > H - 1:
                continue
            
            next_loc = cur_loc.copy()
            for _ in range(n):
                next_loc[0] += 1
                
                if park[next_loc[0]][ next_loc[1]] == "X":
                    fail = 1
                    break
            
            if not fail:
                cur_loc = next_loc.copy()
            fail = 0
        
        elif op == "W":
            if cur_loc[1] - n < 0:
                continue
            
            next_loc = cur_loc.copy()
            for _ in range(n):
                next_loc[1] -= 1
                
                if park[next_loc[0]][ next_loc[1]] == "X":
                    fail = 1
                    break
            
            if not fail:
                cur_loc = next_loc.copy()
            fail = 0
        else:
            if cur_loc[1] + n > W - 1:
                continue
            
            next_loc = cur_loc.copy()
            for _ in range(n):
                next_loc[1] += 1
                
                if park[next_loc[0]][ next_loc[1]] == "X":
                    fail = 1
                    break
            
            if not fail:
                cur_loc = next_loc.copy()
            fail = 0
        
        
    return cur_loc