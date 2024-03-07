def solution(a, b, n):
    answer = 0
    new_coke = 0
    
    while n >= a:
        save_coke = n % a
        n = ((n - save_coke) // a) * b
        answer += n
        n += save_coke

    return answer