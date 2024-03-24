from collections import defaultdict

def solution(survey, choices):
    answer = ''
    survey_dict = defaultdict(int)
    for survey_type, score in zip(survey, choices):
        score_calculated = score - 4
        if score_calculated > 0:
            survey_dict[survey_type[1]] += score_calculated

        else:
            survey_dict[survey_type[0]] += -score_calculated

    
    survey_list = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    
    for front_t, back_t in survey_list:
        if survey_dict[front_t] < survey_dict[back_t]:
            answer += back_t
        else:
            answer += front_t
    
    return answer