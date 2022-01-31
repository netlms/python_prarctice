"""
매개변수로 받은 정수를 한국어로 표기한 문자열을 반환하는 함수 korean_number()를 정의하세요. 단, 매개변수는 1 이상 10 이하의 정수라고 가정합니다.
"""

def korean_number(num):
    kor_expression = ['일', '이', '삼', '사', '오', '육', '칠', '팔', '구', '십']
    return (kor_expression[num - 1])

for i in range (1, 11):
    print(korean_number(i))

# def korean_number(num):
#     if num == 1:
#         return '일'
#     elif num == 2:
#         return '이'
#     elif num == 3:
#         return '삼'
#     elif num == 4:
#         return '사'
#     elif num == 5:
#         return '오'
#     elif num == 6:
#         return '육'
#     elif num == 7:
#         return '칠'
#     elif num == 8:
#         return '팔'
#     elif num == 9:
#         return '구'
#     elif num == 10:
#         return '십'