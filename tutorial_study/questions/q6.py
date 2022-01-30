"""
다음 코드1를 읽고, 실행 결과를 알아맞혀 보세요.

number = 358

rem = rev = 0
while number >= 1:
    rem = number % 10
    rev = rev * 10 + rem
    number = number // 10

print(rev)
"""

# 출력값: 853 
# number 값을 % 연산하여 1의 자리 수를 rev에 저장, 이후 while문을 통해 반복하며 계속하여 number의 1의 자리 수를 rev에 저장하며 기존에 rev에 있던 값은 10을 곱하여 올림
# while 문을 돌며 rev 값은 8, 85, 853 순으로 변화, 최종적으로 rev값은 853이 되며 이를 출력