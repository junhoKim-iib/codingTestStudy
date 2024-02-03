def solution(s):
    answer = 0
    def find_split_point(s):
        same_cnt = 0
        diff_cnt = 0
        for char in s:
            if char == s[0]:
                same_cnt += 1
            else:
                diff_cnt += 1
            if same_cnt == diff_cnt:
                return same_cnt + diff_cnt
        return len(s)

    while s:
        split_point = find_split_point(s)
        answer += 1
        s = s[split_point:]

    return answer


