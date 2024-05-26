def date_to_day(date):
    year, month, day =map(int,date.split('.')) 
    total_day = year * 28 * 12 + month * 28 + day
    
    return total_day


def solution(today, terms, privacies):
    answer = []
    today = date_to_day(today)
    privacies_day = [[date_to_day(x.split(" ")[0]), x.split(" ")[1]] for x in privacies]
    
    terms_dict = {x.split(" ")[0]:int(x.split(" ")[1]) for x in terms}

    for i,privacy in enumerate(privacies_day):
        if today >= terms_dict[privacy[1]] * 28 + privacy[0]:
            answer.append(i+1)

    return answer