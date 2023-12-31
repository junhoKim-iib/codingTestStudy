def solution(numbers):
    stack = []          # 모노톤 스택을 사용할 스택
    answer = [-1] * len(numbers)  # 각 원소에 대한 답을 저장할 배열 초기화

    for i in range(len(numbers)):
        # 현재 원소보다 작은 값을 가진 스택의 원소들을 처리
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()  # 스택의 가장 위에 있는 인덱스를 꺼내옴
            answer[idx] = numbers[i]  # 해당 인덱스에 대한 답 갱신
        stack.append(i)  # 현재 인덱스를 스택에 추가

    return answer
