"""
나는야 포켓몬 마스터 이다솜
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
from collections import defaultdict

n, m = map(int, input().split())

book_by_index = defaultdict(str)
book_by_name = defaultdict(int)

for i in range(1, n + 1):
    a = input()
    book_by_index[i] = a
    book_by_name[a] = i

for i in range(m):
    question = input()
    if question.isdigit():
        print(book_by_index[int(question)])
    else:
        print(book_by_name[question])
