"""
문제 1. calendar 모듈을 임포트하는 문장을 완성하세요.
>>> ____ calendar

calendar 모듈에 무엇이 있는지 살펴보세요.
>>> dir(calendar)
['Calendar', 'EPOCH', 'FRIDAY', 'February', 'HTMLCalendar', 'IllegalMonthError', 'IllegalWeekdayError', 'January', 'LocaleHTMLCalendar', 'LocaleTextCalendar', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'TextCalendar', 'WEDNESDAY', '_EPOCH_ORD', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_colwidth', '_locale', '_localized_day', '_localized_month', '_monthlen', '_nextmonth', '_prevmonth', '_spacing', 'c', 'calendar', 'datetime', 'day_abbr', 'day_name', 'different_locale', 'error', 'firstweekday', 'format', 'formatstring', 'isleap', 'leapdays', 'main', 'mdays', 'month', 'month_abbr', 'month_name', 'monthcalendar', 'monthrange', 'prcal', 'prmonth', 'prweek', 'repeat', 'setfirstweekday', 'sys', 'timegm', 'week', 'weekday', 'weekheader']

이와 같이 모듈은 수많은 공구가 들어 있는 '공구통'이라고 생각할 수 있습니다.

문제 2. calendar 모듈에 leap이라는 문자열을 포함하는 이름은 어떤 것이 있는지 찾아보세요.
>>> [x for x in dir(calendar) if 'leap' in x]
[____, ____]

문제 3. 주어진 해가 윤년인지 아닌지 판별하는 함수의 사용법을 확인해보세요.
>>> help(____)
Help on function ____ in module calendar:

____(year)
    Return True for leap years, False for non-leap years.
    
문제 4. 이 함수를 사용해서 2077년이 윤년인지 아닌지 확인해보세요.
>>> ____
False
"""

# Q1
import calendar

calendar.prmonth(2000, 12)

print(dir(calendar))

# Q2
print(list(x for x in dir(calendar) if 'leap' in x))

# Q3
help(calendar.isleap)           # help() shows manual for the argument (func, method, keyword, module)

print(calendar.isleap(2077))