def solution(friends, gifts):
    answer = 0
    gift_table = [[0 for _ in range(len(friends))] for _ in range(len(friends)) ]
    next_month_list = [0 for _ in range(len(friends))]
    
    
    for item in gifts:
        A, B = item.split()
        gift_table[friends.index(A)][friends.index(B)] += 1
    
    gift_get_list = [sum(col) for col in zip(*gift_table)]
    gift_give_list = [sum(row) for row in gift_table]
    gift_difference_list = [give - get for get, give in zip(gift_get_list, gift_give_list)]

    for i in range(len(gift_table)):
        for j in range(len(gift_table[0])):
            if gift_table[i][j] > gift_table[j][i]:
                next_month_list[i] += 1
               
            elif gift_table[i][j] == gift_table[j][i]:
                if gift_difference_list[i] > gift_difference_list[j]:
                    next_month_list[i] += 1
            
            
    return max(next_month_list)