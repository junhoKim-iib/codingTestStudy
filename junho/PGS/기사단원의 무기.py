def solution(number, limit, power):

    answer = [1 for i in range(number+1)]
    answer[0] = 0
    for i in range(2, number + 1):
        
        for j in range(i, number + 1, i):
            answer[j] += 1
            
    for i in range(len(answer)):
        if answer[i] > limit:
            answer[i] = power

    return sum(answer)

