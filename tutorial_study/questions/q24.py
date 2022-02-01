"""
나눗셈을 이용해 십진수를 이진수로 변환하는 방법은 다음과 같습니다.

십진수를 2로 나눈 몫을 구하고 그 수를 다시 2로 나누는 일을 몫이 0이 될 때까지 반복하고, 각 단계에서 구한 나머지를 거꾸로 쓰면 이진수가 됩니다.

예를 들어, 십진수 13에 해당하는 이진수를 구하는 과정을 아래와 같이 나타낼 수 있습니다.

>>> divmod(13, 2) # 13을 2로 나눈 몫은 6, 나머지는 1
(6, 1)
>>> divmod(6, 2) # 6을 2로 나눈 몫은 3, 나머지는 0
(3, 0)
>>> divmod(3, 2) # 3을 2로 나눈 몫은 1, 나머지도 1
(1, 1)
>>> divmod(1, 2) # 1을 2로 나눈 몫은 0, 나머지는 1
(0, 1)

위의 각 단계에서 구한 나머지 1, 0, 1, 1을 역순으로 쓴 1101이 십진수 13에 해당하는 이진수입니다. 
파이썬의 bin() 함수를 이용하면 위와 같이 번거로운 계산을 직접 하지 않고도 이진수를 쉽게 구할 수 있죠.
>>> bin(13)
'0b1101'

0b는 뒤의 숫자가 이진수임을 나타냅니다.

문제
십진수를 입력받아 그 숫자에 해당하는 이진수의 각 자리를 리스트로 출력하는 프로그램을 작성하세요. (순서에 유의)

예1
입력:

13
출력:

[1, 1, 0, 1]
예2
입력:

87
출력:

[1, 0, 1, 0, 1, 1, 1]
"""

if __name__ == '__main__':
    num = int(input())
    bin = []

    while True:
        if num == 0:
            if len(bin) < 1:
                bin.insert(0, 0)
            break
        else:
            bin.insert(0, num % 2)
            num = num // 2

    print(bin)

# d = int(input())
# m = d
# b = []

# while True:
#     d, m = divmod(d, 2)
#     b.insert(0, m)
#     if d == 0:
#         break

# print(b)