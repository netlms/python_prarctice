"""
다음 예와 같이 구구단을 2단부터 9단까지 계산해서 출력하는 프로그램을 짜보세요. 

예
출력:

2 * 1 = 2
2 * 2 = 4
…        
9 * 9 = 81
"""

for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}')

# def multiply(num):
#     for i in range(1, 10):
#         print(f'{num} * {i} = {num * i}')

# for i in range(2, 10):
#     multiply(i)