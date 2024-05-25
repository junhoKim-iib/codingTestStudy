def solution(book_time):
    answer = 0
    room_list = []
    book_time = sorted(book_time, key=lambda x:"".join(x[0].split(':')))

    
    for book in book_time:
        start_time = book[0].split(":")
        start_time = int(start_time[0]) * 60 + int(start_time[1])
        
        end_time = book[1].split(":")
        end_time = int(end_time[0]) * 60 + int(end_time[1]) + 10
             
        done_flag = 0

        for room in room_list:
            if room[-1] <= start_time:
                room.append(end_time)
                done_flag = 1
                break

        if not done_flag:
            room_list.append([end_time])
            answer += 1
            done_flag = 0
                    
    
    return answer