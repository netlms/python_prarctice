"""
대학교의 화학자들은 상처를 매우 빠르게 치료하는 약물을 제조하는 새로운 과정을 개발했다. 
제조 과정은 매우 길고 화학 약품을 매번 모니터링해야 하므로 몇 시간씩 걸린다! 
학생들은 졸거나 딴짓을 하므로 이 일을 믿고 맏길 수가 없다. 
그러므로 약물의 제조를 모니터링하는 자동 장치를 프로그래밍해야 한다. 장치는 15초마다 온도를 측정해 프로그램에 제공한다.

프로그램은 먼저 최소와 최대의 안전 온도를 나타내는 두 개의 정수를 읽는다. 그 다음에, 장치가 제공하는 온도(정수)를 계속 읽는다. 
화학 반응이 완료되면 장치는 끝을 알리는 -999를 보낸다. 
기록된 온도가 올바른 범위에 있을 경우(최솟값 또는 최댓값과 같아도 된다) Nothing to report를 표시해야 한다. 
하지만 온도가 위험 수준에 도달하면 Alert!를 표시하고 온도 측정을 중단한다(장치가 온도값을 계속 보내더라도).

예 1
입력:

10 20
15 10 20 0 15 -999
출력:

Nothing to report
Nothing to report
Nothing to report
Alert!

예 2
입력:

0 100
15 50 75 -999
출력:

Nothing to report
Nothing to report
Nothing to report

힌트
split() 메서드를 사용해 문자열을 분할한 리스트를 얻을 수 있습니다.

>>> '0 100'.split()
['0', '100']

다음과 같이 split()으로 얻은 결과를 바로 변수에 할당할 수 있습니다.

>>> freezing_point, boiling_point = '0 100'.split()
>>> freezing_point
'0'
>>> boiling_point
'100'

input()으로 문자열을 입력받을 때에도, 문자열을 분할했을 때 리스트 원소가 몇 개가 될지 미리 정해져 있다면 위와 같은 방법으로 변수에 할당할 수 있습니다. 
원소 개수를 미리 알 수 없다면 for 문을 이용하세요.
"""

low, high = input().split()

low = int(low)
high = int(high)

arr = input().split()

arr = list(map(int, arr))

for i in arr:
    if i == -999:
        break
    elif i < low or high < i:
        print("Alert!", i)
        break
    elif low <= i and i <= high:
        print("Nothing to report", i)

# L = input().split()
# min = int(L[0])
# max = int(L[1])

# temp = int(input())

# while temp != -999:
#     if min <= temp <= max:
#         print('Nothing to report')
#         temp = int(input())
#     else:
#         print('Alert!')
#         break