"""
상어 초등학교
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
n = int(input())
favorite_student = []
board = [[0] * n for _ in range(n)]

for _ in range(n ** 2):
    array = list(map(int, input().split()))
    favorite_student.append((array[0], array[1:]))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for student, likes in favorite_student:
    max_count = 0
    one_rule = []
    for x in range(n):
        for y in range(n):
            if board[x][y] > 0:
                continue
            count = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx >= 0 and ny >= 0 and nx < n and ny < n:
                    if board[nx][ny] in likes:
                        count += 1
            if count > max_count:
                max_count = count
                one_rule = []
                one_rule.append((x, y))
            elif count == max_count:
                one_rule.append((x, y))

    if len(one_rule) == 1:
        board[one_rule[0][0]][one_rule[0][1]] = student
    else:
        max_empty = 0
        two_rule = []
        for x, y in one_rule:
            if board[x][y] > 0:
                continue
            empty = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx >= 0 and ny >= 0 and nx < n and ny < n:
                    if board[nx][ny] == 0:
                        empty += 1
            if empty > max_empty:
                max_empty = empty
                two_rule = []
                two_rule.append((x, y))
            elif empty == max_empty:
                two_rule.append((x, y))
        
        for x, y in two_rule:
            if board[x][y] > 0:
                continue
            else:
                board[x][y] = student
                break

like = dict()
for student, likes in favorite_student:
    like[student] = likes

result = 0
        
for x in range(n):
    for y in range(n):
        count = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if board[nx][ny] in like[board[x][y]]:
                    count += 1
        if count == 0:
            result += 0
        elif count == 1:
            result += 1
        elif count == 2:
            result += 10
        elif count == 3:
            result += 100
        elif count == 4:
            result += 1000

print(result)
