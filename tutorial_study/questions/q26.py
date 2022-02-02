"""
매개변수로 입력받은 정수에 해당하는 영문 문자열을 반환하는 함수 korean_number()를 if 문을 사용하지 말고 작성하세요. 단, 사용자는 0 이상 9 이하의 정수 중 하나를 입력한다고 가정합니다.
"""

def eng_number(num):
    int_to_word = {0 : '영', 1 : '일', 2 : '이', 3 : '삼', 4 : '사', 5 : '오', \
        6 : '육', 7 : '칠', 8 : '팔', 9 : '구'}
    return (int_to_word[num])

if __name__=='__main__':
    print(eng_number(int(input())))

# def korean_number(num):
#     d = {0: '영', 1: '일', 2: '이', 3: '삼', 4: '사', 5: '오', 6: '육', 7: '칠', 8: '팔', 9: '구'}
#     return d[num]