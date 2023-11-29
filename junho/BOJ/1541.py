import sys
import re 

input = sys.stdin.readline

input_str = input().strip()

# 숫자를 기준으로 문자열 분리
op_list = list(filter(None, re.split(r'\d+', input_str)))

# '-'와 '+'를 기준으로 문자열 분리
n_list = re.split(r'[-+]', input_str)

# 먼저 + 연산을 모두 진행
i = 0
while i < len(op_list):
    op = op_list[i]
    if op == '+':
        sum_result = int(n_list[i]) + int(n_list[i + 1])
        n_list.pop(i)
        n_list.pop(i)
        op_list.pop(i)
        n_list.insert(i, sum_result)
    else:
        i += 1

res = int(n_list[0])

# 리스트의 길이가 1보다 크다면 뺄셈 연산이 남아있는 것.
if len(n_list) > 1:
    for n in n_list[1:]:
        res -= int(n)

print(res)