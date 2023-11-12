import sys

input = sys.stdin.readline

N = int(input())
book_dict = {}
for _ in range(N):
    title = input().strip()
    if title in book_dict:
        book_dict[title] += 1
    else:
        book_dict[title] = 1

book_tuple_list = sorted(book_dict.items())
book_tuple_list = sorted(book_tuple_list, key=lambda x: x[1], reverse=True)
print(book_tuple_list[0][0])