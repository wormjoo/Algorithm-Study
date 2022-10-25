"""
최소 힙
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
import heapq
import sys

n = int(input())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline()) # input() 사용 시 시간 초과
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)
