"""
직각삼각형의 두 직각변 , 를 각각 한 변으로 하는 정사각형 면적의 합은 빗변(hypotenuse) 를 한 변으로 하는 정사각형의 면적과 같습니다. 
이를 ‘피타고라스 정리’라고 합니다. (위키백과)

a^2 + b^2 = c^2


a와 b의 길이를 알면 c의 길이를 구할 수 있습니다.


문제 1
a = 3, b = 4일 때 c가 얼마인지 파이썬 셸에서 구하세요.

문제 2
두 직각변(a, b)의 길이를 입력으로 받아 빗변(c)의 길이를 구하는 함수 hypotenuse()를 작성하세요. 출력은 소수점 셋째 자리에서 반올림합니다.
>>> hypotenuse(3, 4)
5.0
>>> hypotenuse(10, 20)
22.36
"""

# Q1
import math

if __name__ == '__main__':
    a, b = 3, 4

    print(math.sqrt(pow(a, 2) + pow(b, 2)))     # pow(a, b) returns a ** b

# Q2

def hypotenuse(a, b):
    import math
    return (round(math.sqrt(pow(a, 2) + pow(b, 2)), 2))

if __name__ == '__main__':
    print(hypotenuse(3, 4))
    
# # Q1
# import math
# math.sqrt(3**2 + 4**2)

# # Q2
# import math

# def hypotenuse(a, b):
#     c = math.sqrt(a**2 + b**2)
#     return round(c, 2)
    
# if __name__ == '__main__':
#     print(hypotenuse(3, 4))
#     print(hypotenuse(10, 20))