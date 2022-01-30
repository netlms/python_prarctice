"""
input()으로 사용자로부터 입력받은 정수를 계속 더해나가다가, 음수가 입력되면 중단하고 그 전까지 계산한 값을 출력하는 파이썬 스크립트를 작성하세요.
"""

num = 0
sum = 0

while num >= 0:
    sum += num
    num = int(input())

print(sum)


# sum = 0
# while True:
#     num = int(input())
#     if num < 0:
#         break
#     else:
#        sum += num

# print(sum)