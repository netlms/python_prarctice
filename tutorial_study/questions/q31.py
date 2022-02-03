"""
다음은 2021년 2월의 달력을 변수 m으로 저장하고 화면에 출력하는 코드입니다. 빈칸을 채우세요.

import calendar
c = calendar.TextCalendar()
m = c.███████████(2021, 2)
print(m)
결과:

   February 2021
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
"""

import calendar

# help(calendar.TextCalendar)

c = calendar.TextCalendar()
m = c.formatmonth(2021, 2)
print(m)


# import calendar

# c = calendar.TextCalendar()
# m = c.formatmonth(2021, 2)
# print(m)