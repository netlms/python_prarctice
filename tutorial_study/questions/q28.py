"""
주사위 두 개가 있습니다. 한 개는 평범한 주사위인데, 다른 한 개의 각 면에는 2에서 13까지의 소수가 적혀 있습니다. 아래 코드는 두 주사위의 눈을 튜플 dice1과 dice2로 나타냅니다.

dice1 = (1, 2, 3, 4, 5, 6)
dice2 = (2, 3, 5, 7, 11, 13)
두 주사위를 던졌을 때 눈의 합으로 나올 수 있는 숫자를 모두 출력하세요. 단, 같은 숫자는 한 번만 출력합니다.
"""

dice1 = (1, 2, 3, 4, 5, 6)
dice2 = (2, 3, 5, 7, 11, 13)

sum = set()

for i in dice1:
    for j in dice2:
        sum.add(i + j)

print(sum)


# dice1 = (1, 2, 3, 4, 5, 6)
# dice2 = (2, 3, 5, 7, 11, 13)

# sum_of_the_two_dice = set()

# for x in dice1:
#     for y in dice2:
#         sum_of_the_two_dice.add(x + y)

# print(sum_of_the_two_dice)