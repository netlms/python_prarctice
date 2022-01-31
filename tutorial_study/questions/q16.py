"""
오늘의 날짜 객체를 구하는 코드는 다음과 같습니다. (코드를 이해하지 못해도 이 문제를 풀 수 있습니다.)

>>> from datetime import datetime
>>> today = datetime.today()
>>> today
datetime.datetime(2021, 3, 21, 15, 46, 1, 94942)
위 코드의 today에서 연도를 구하는 방법은 다음과 같습니다.

>>> today.year
2021
태어난 해를 네 자리 숫자로 입력하면 한국 나이를 반환하는 함수 korean_age()를 작성하세요.
"""

from datetime import datetime

def korean_age(birth):
    today = datetime.today()
    return(today.year - birth + 1)

print(korean_age(1993))

# def korean_age(birth_year):
#     from datetime import datetime
#     today = datetime.today()
#     return today.year - birth_year + 1