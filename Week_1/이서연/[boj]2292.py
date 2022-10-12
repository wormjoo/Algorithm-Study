'''
벌집

- 문제 요약
육각형으로 이루어진 벌집.
중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 
숫자 N이 주어졌을때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈때 몇개의 방을 지나가는지(시작과 끝을 포함하여) 계산하는 프로그램.

- 입력 조건
첫째 줄에 N(1<= N <= 1,000,000,000)이 주어짐

- 출력 조건
입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇개의 방을 지나는지 출력
'''
n = int(input())
# 인접한 방이 6의 배수로 증가
# 1 -> 1 (지나가는 방의 수)
# 1 + 6 -> 2
# 1 + 6 + 12 -> 3
i = 1
room = 1
n = n - 1 # 1번 방
while n > 0:
    n -= 6*i
    room += 1
    i += 1
print(room)
