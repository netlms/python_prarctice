"""
어떤 수(number)의 각 자리 숫자(digit)의 합을 계산하는 sumOfDigits()라는 재귀 함수를 작성하자. 이번에는 리스트와 map() 함수를 이용해서 풀어보세요.
입력한 수를 읽어 sumOfDigits() 함수를 호출하며, 이 함수는 합산할 숫자가 남지 않을 때까지 자신을 호출해, 최종적인 합을 사용자에게 표시한다.

sumOfDigits()는 다음과 같은 원리로 작동한다.(주의: 실제 코드가 아님)

sumOfDigits(6452) = 2 + sumOfDigits(645)
sumOfDigits(645) = 5 + sumOfDigits(64)
...
sumOfDigits(6) = 6

예 1
입력:

47253
출력:

21

예 2
입력:

643
출력:

13
"""

# # using recursive
# def sumOfDigits(num):
#     while True:
#         if num < 10:
#             return num
#         else:
#             return (sumOfDigits(num // 10) + num % 10)
        

# print(sumOfDigits(int(input())))

# using list, map()

def sumOfDigits(num):
    arr = map(int, num)
    return (sum(arr))

print(sumOfDigits(input()))

# def sumOfDigits(num):
#     digits = map(int, list(str(num)))
#     return sum(digits)

# if __name__ == '__main__':
#     print(sumOfDigits(47253))
#     print(sumOfDigits(643))