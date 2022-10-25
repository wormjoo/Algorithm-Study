"""
케빈 베이컨의 6단계 법칙
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
from collections import deque
INF = 1e9

def bfs(graph, start):
    queue = deque([start])
    visited = [start]
    count = [0] * (n + 1)

    while queue:
        v = queue.popleft()
        for i in sorted(graph[v]):
            if i not in visited:
                count[i] += count[v] + 1
                queue.append(i)
                visited.append(i)
    
    return sum(count)
        

n, m = map(int, input().split())
bacon = [int(INF)] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    bacon[i] = bfs(graph, i)

print(bacon.index(min(bacon)))
