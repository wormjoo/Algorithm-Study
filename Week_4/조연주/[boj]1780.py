"""
종이의 개수
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
def paper(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if matrix[i][j] != matrix[x][y]:
                paper(x, y, n // 3)
                paper(x + n // 3, y, n // 3)
                paper(x + n // 3 * 2, y, n // 3)
                paper(x, y + n // 3, n // 3)
                paper(x + n // 3, y + n // 3, n // 3)
                paper(x + n // 3 * 2, y + n // 3, n // 3)
                paper(x, y + n // 3 * 2, n // 3)
                paper(x + n // 3, y + n // 3 * 2, n // 3)
                paper(x + n // 3 * 2, y + n // 3 * 2, n // 3)
                return
    
    if matrix[x][y] == -1:
        result[0] += 1
    elif matrix[x][y] == 0:
        result[1] += 1
    else:
        result[2] += 1

n = int(input())
matrix = []
result = [0, 0, 0]

for _ in range(n):
    matrix.append(list(map(int, input().split())))

paper(0, 0, n)

for i in range(3):
    print(result[i])
