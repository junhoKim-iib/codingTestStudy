def solution(numbers):
    sorted_numbers = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)

    if sorted_numbers[0] == '0':
        return '0'
    
    return ''.join(sorted_numbers)

