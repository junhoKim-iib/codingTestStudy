def solution(food):
    water = '0'

    front = ''.join(str(i) * (n//2) for i,n in enumerate(food))    
    back = front[::-1]
        
    return front + water + back