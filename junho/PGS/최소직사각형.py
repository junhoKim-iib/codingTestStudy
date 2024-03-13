def solution(sizes):
    max_x, max_y = 0,0
    for element in sizes:
        element = sorted(element)
        
        max_x = element[0] if max_x < element[0] else max_x
        max_y = element[1] if max_y < element[1] else max_y
        
    return max_x * max_y