"""
정수를 한 개 입력받아 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을 작성해 보세요. 단, 이번에는 for 문을 사용하세요.
"""

num = int(input())

for i in range (1, num + 1):
    print(i, i * i)