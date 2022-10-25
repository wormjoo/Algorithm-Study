"""
팩토리얼 0의 개수
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
def facto(n):
    if n <= 1:
        return 1
    return n * facto(n - 1)

n = int(input())
factorial_n = str(facto(n))
length = len(factorial_n)
count = 0

for x in range(1, length + 1):
    if factorial_n[-x] == '0':
        count += 1
    else:
        break

print(count)
