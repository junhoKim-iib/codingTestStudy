def can_create_goal(cards1, cards2, goal):
    def backtrack(cards1, cards2, goal):
        if not goal:
            return True

        if cards1 and cards1[0] == goal[0] and backtrack(cards1[1:], cards2, goal[1:]):
            return True

        if cards2 and cards2[0] == goal[0] and backtrack(cards1, cards2[1:], goal[1:]):
            return True

        return False

    return backtrack(cards1, cards2, goal)


def solution(cards1, cards2, goal):
    answer = ''
    result = can_create_goal(cards1, cards2, goal)
    if result == True:
        answer = "Yes"
    else:
        answer = "No"

    return answer