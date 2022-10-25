"""
유기농 배추
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
import sys
sys.setrecursionlimit(10**6) # 제한없으면 recursive error

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    if x <= -1 or x>= n or y <= -1 or y >= m:
        return False
    if board[x][y] == 1:
        board[x][y] = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            dfs(nx, ny)
        return True
    return False

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]

    for i in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    print(result)
