"""
잃어버린 괄호
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
expression = list(map(str, input().split('-')))
plus = 0
minus = 0

plus = sum(list(map(int, expression[0].split('+'))))

for i in range(1, len(expression)):
    minus += sum(list(map(int, expression[i].split('+'))))

print(plus - minus)
