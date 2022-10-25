"""
피보나치 함수
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
t = int(input())
zero = [1, 0]
one = [0, 1]

for i in range(2, 41):
    zero.append(zero[i - 1] + zero[i - 2])
    one.append(one[i - 1] + one[i - 2])

for _ in range(t):
    n = int(input())
    print(zero[n], one[n])
