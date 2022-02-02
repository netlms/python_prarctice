"""
사용자로부터 날짜를 나타내는 세 개의 숫자를 입력받습니다. 첫 번째 숫자는 연도를 나타내는 네 자리 숫자이고, 두 번째 숫자는 월을, 세 번째 숫자는 일을 나타냅니다.

입력받은 날짜를 mm/dd/yyyy 형식으로 출력합니다. 월을 두 자리 숫자(01, 02, 03, ..., 12)로, 일을 두 자리 숫자(01, 02, 03, ..., 31)로, 연도를 네 자리 숫자로 나타냅니다.

입력받은 날짜의 다음 날에 해당하는 날짜도 같은 형식으로 출력합니다. 단, 윤년은 무시합니다(2월은 항상 28일까지 있다고 가정합니다).

예 1
입력:

2018 10 2
출력:

10/02/2018
10/03/2018

예 2
입력:

2018 10 31
출력:

10/31/2018
11/01/2018

예 3
입력:

2018 11 30
출력:

11/30/2018
12/01/2018

예 4
입력:

2018 12 31
출력:

12/31/2018
01/01/2019
"""

if __name__=='__main__':
    year, month, day = input().split()

    print(f'{month}/{day}/{year}')

    year = int(year)
    month = int(month)
    day = int(day)

    if month == 2 and day == 28:
        month = 3
        day = 1
    elif day == 30 and (month == 4 or month == 6 or month == 9 or month == 11):
        day = 1
        month += 1
    elif day == 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10):
        day = 1
        month += 1
    elif day == 31 and month == 12:
        year += 1
        day = 1
        month = 1
    else:
        day += 1

    print(str(month).zfill(2), str(day).zfill(2), year)
# 튜플을 배운 챕터에서 나온 문제이나 정확히 튜플을 써야 할 부분을 찾지 못함


# def read_date():
#     year, month, day = tuple(map(int, input().split()))
#     return year, month, day

# def print_date(date):
#     year, month, day = date
#     print("%02d/%02d/%04d" % (month, day, year))

# def advance_day(date):
#     year, month, day = date
    
#     # end_of_month = (month == 1 and day == 31) or \
#                # (month == 2 and day == 28) or \
#                # (month == 3 and day == 31) or \
#                # (month == 4 and day == 30) or \
#                # (month == 5 and day == 31) or \
#                # (month == 6 and day == 30) or \
#                # (month == 7 and day == 31) or \
#                # (month == 8 and day == 31) or \
#                # (month == 9 and day == 30) or \
#                # (month == 10 and day == 31) or \
#                # (month == 11 and day == 30) or \
#                # (month == 12 and day == 31)
    
#     #end_of_month = (month in [1, 3, 5, 7, 8, 10, 12] and day == 31) or \
#     #                     (month in [4, 6, 9, 11] and day == 30) or \
#     #                     (month == 2 and day == 28)
    
#     end_of_month = (month, day) in [(1, 31), (2, 28), (3, 31), (4, 30), (5,
#         31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]
    
#     end_of_year = month == 12 and day == 31
    
#     if end_of_month:
#         if end_of_year:
#             year += 1
#             month = 1
#             day = 1
#         else:
#             month += 1
#             day = 1
#     else:
#         day += 1
    
#     return year, month, day
    
# if __name__ == "__main__":
#     today = read_date()
#     print_date(today)
#     tomorrow = advance_day(today)
#     print_date(tomorrow)
# 답안에서는 각 달의 끝 날짜를 튜플 형태로 만들어 입력 날짜와 비교함. 조건문을 길게 쓰는 것보다 가독성이 좋고 더 간결해짐.