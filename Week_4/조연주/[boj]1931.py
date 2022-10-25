"""
회의실 배정
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
import sys

n = int(input())
information = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    information.append((start, end))

information.sort()
current = information[0]
count = 1

for element in information[1:]:
    start, end = element
    if current[1] > end:
        current = element
        continue
    if current[1] <= start:
        current = element
        count += 1

print(count)
