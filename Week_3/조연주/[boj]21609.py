"""
상어 중학교
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
from collections import deque

n, m = map(int, input().split())
array = []
score = 0

for _ in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y, checked, visited, current):
    queue = deque()
    queue.append([x, y])
    blocks = [[x, y]]
    total_count, rainbow_count = 1, 0
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if (0 <= nx < n and 0 <= ny < n) and (not visited[nx][ny]) :
                if array[nx][ny] == 0:
                    visited[nx][ny] = True
                    rainbow_count += 1
                    total_count += 1
                    queue.append([nx, ny])
                    blocks.append([nx, ny])
                elif array[nx][ny] == current:
                    visited[nx][ny] = True
                    checked[nx][ny] = True
                    total_count += 1
                    queue.append([nx, ny])
                    blocks.append([nx, ny])
    
    return total_count, rainbow_count, blocks

def find_block_group():
    block_group = []
    checked = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            visited = [[False] * n for _ in range(n)]
            if array[i][j] > 0 and not checked[i][j]:
                checked[i][j] = True
                total_count, rainbow_count, blocks = bfs(i, j, checked, visited, array[i][j])
                if total_count >= 2:
                    block_group.append([total_count, rainbow_count, blocks])

    block_group.sort(reverse=True)
    return block_group
    
def gravity(array):
    new_array = [[-2] * n for _ in range(n)]
    for x in range(n - 1, -1, -1):
        for y in range(n):
            if array[x][y] == -1:
                new_array[x][y] = -1
            elif array[x][y] == -2:
                continue
            else:
                down = 1
                while 1:
                    if x + down >= n or (array[x + down][y] != -2):
                        break
                    down += 1
                new_array[x + down - 1][y] = array[x][y]
                array[x][y] = -2
                array[x + down - 1][y] = new_array[x + down - 1][y]

    return new_array

def rotate(array):
    return list(map(list, zip(*array)))[::-1]

while 1:
    block_group = find_block_group()
    l = len(block_group)

    if l < 1:
        break

    for x, y in block_group[0][2]:
        array[x][y] = -2

    score += block_group[0][0] ** 2
    array = gravity(array)

    array = rotate(array)
    array = gravity(array)

print(score)
