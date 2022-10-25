"""
숨바꼭질
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
from collections import deque

def bfs(current, visited):
    visited[current] = True
    queue = deque([current])
    count = [0] * 100001

    while queue:
        v = queue.popleft()
        if v == k:
            print(count[v])
            break
        for i in (v - 1, v + 1, 2 * v):
            if 0 <= i < 100001 and not visited[i]:
                visited[i] = True
                count[i] = count[v] + 1
                queue.append(i)

n, k = map(int, input().split())

if n >= k:
    print(n - k)
else:
    visited = [False] * 100001
    bfs(n, visited)
