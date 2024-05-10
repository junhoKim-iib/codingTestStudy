from functools import reduce 

def solution(data, col, row_begin, row_end):

    answer = 0
    
    data = sorted(data, key=lambda x :(x[col-1], -x[0]))
    
    answer = reduce(lambda x,y: x ^ y,
                    [sum(map(lambda x : x%(i+1),data[i])) for i in range(row_begin - 1, row_end)])
    
    return answer 