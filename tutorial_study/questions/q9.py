"""
윤년은 역법을 실제 태양년에 맞추기 위해 여분의 하루 또는 월을 끼우는 해입니다. 현재 사용하는 그레고리력의 윤년 규칙은 다음과 같습니다.

서력 기원 연수가 4로 나누어 떨어지는 해는 윤년으로 한다. (1988년, 1992년, 1996년, 2004년, 2008년, 2012년, 2016년, 2020년, 2024년, 2028년, 2032년, 2036년, 2040년, 2044년 ...)
서력 기원 연수가 4, 100으로 나누어 떨어지는 해는 평년으로 한다. (1900년, 2100년, 2200년, 2300년, 2500년...)
서력 기원 연수가 4, 100, 400으로 나누어 떨어지는 해는 윤년으로 둔다. (2000년, 2400년...)

연도를 나타내는 정수를 입력으로 받아서 윤년인지 아닌지 출력하는 프로그램을 작성해 보세요.
"""

year = int(input())

if (year % 4) != 0:
    print("평년")
else:
    if (year % 100) != 0:
        print("윤년")
    else:
        if (year % 400) != 0:
            print("평년")
        else:
            print("윤년")

# while True:
#     is_leap_year = None

#     year = int(input())

#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 is_leap_year = True
#             else:
#                 is_leap_year = False
#         else:
#             is_leap_year = True
#     else:
#         is_leap_year = False

#     if is_leap_year:
#         print(f'{year} is a leap year')
#     else:
#         print(f'{year} is not a leap year')