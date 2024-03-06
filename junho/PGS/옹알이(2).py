def solution(babbling):
    answer = 0
    word_list = ["aya", "ye", "woo", "ma"]
    wrong_list = ["ayaaya", "yeye", "woowoo", "mama"]
    
    for word in babbling:
        for i in range(len(word_list)):
            if word_list[i] in word:
                if wrong_list[i] not in word:
                    word = word.replace(word_list[i]," ")

        if word.strip() == "":
            answer += 1
    return answer