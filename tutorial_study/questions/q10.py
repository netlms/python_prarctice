"""
사용자로부터 input()으로 정수를 한 개 입력받아, 그 숫자를 숫자 크기만큼 반복해서 출력하는 파이썬 스크립트를 작성하세요. 이때 출력 앞에 공백을 한 칸 주어서, 입력과 출력이 구분되게 합니다.
단, 이번에는 for 문을 사용하세요.
"""

num = int(input())

for i in range(0, num):
    print(" ", num)

# num = int(input())

# for i in range(num):
#     print(" ", num)