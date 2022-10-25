"""
듣보잡
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
from collections import defaultdict

n, m = map(int, input().split())
people = defaultdict(int)

for _ in range(n):
    people[input()] += 1

for _ in range(m):
    people[input()] += 1

strangers = [person for person in people.keys() if people[person] == 2]
strangers.sort()

print(len(strangers))
for stranger in strangers:
    print(stranger)
