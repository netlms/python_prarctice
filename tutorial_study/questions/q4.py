"""
정수를 한 개 입력받아, 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을 작성해 보세요. 단, while 문을 사용하세요.
"""

num = int(input())

count = 1
while count <= num:
    print(count, count * count)
    count += 1