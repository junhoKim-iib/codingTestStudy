from functools import reduce 

def solution(data, col, row_begin, row_end):

    S_i_list = []
    
    data = sorted(data, key=lambda x : x[0], reverse=True)
    data = sorted(data, key=lambda x:x[col-1])
    
    for i in range(row_begin - 1, row_end):
        S_i_list.append(sum(val%(i+1) for val in data[i]))
    
    
    return reduce(lambda x,y : x^y, S_i_list)