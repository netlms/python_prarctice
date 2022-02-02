"""
ord()와 chr()

ord() 함수는 문자에 해당하는 코드값을 알려줍니다.
>>> ord('A')
65
>>> ord('Z')
90
>>> ord('a')
97
>>> ord('z')
122
>>> ord('0')
48
>>> ord('9')
57

역으로, chr() 함수에 코드값을 입력으로 넣으면 그에 해당하는 문자를 얻습니다.
>>> chr(65)
'A'

한글에 대해서도 두 함수를 사용할 수 있습니다.
>>> ord('가')
44032
>>> chr(55197)
'힝'

split()은 공백을 기준으로 문자열을 분리한 것들을 리스트에 넣어 반환합니다.

>>> 'hello world'.split()
['hello', 'world']
여러 행으로 이뤄진 문자열을 분리하려면 \n을 구분자로 지정합니다.
>>> love = '''L is for the way you look at me
... O is for the only one I see
... V is very, very extraordinary
... E is even more than anyone that you adore can'''
>>> love.split('\n')
['L is for the way you look at me', 'O is for the only one I see', 'V is very, very extraordinary', 'E is even more than anyone that you adore can']

문제

다음 txt는 정신질환의 명칭을 한국어와 영어 용어로 나열한 것입니다.

txt = '''신경발달장애 Neurodevelopmental Disorders
조현병 스펙트럼 및 기타 정신병적 장애 Schizophrenia Spectrum and Other Psychotic Disorders
양극성 및 관련 장애 Bipolar and Related Disorders
우울장애 Depressive Disorders
불안장애 Anxiety Disorder
강박 및 관련 장애 Obsessive－Compulsive and Related Disorders
외상 및 스트레스 관련 장애 Trauma－and Stressor－Related Disorders
해리장애 Dissociative Disorders
신체증상 및 관련 장애 Somatic Symptom and Related Disorders
급식 및 섭식장애 Feeding and Eating Disorders
배설장애 Elimination Disorders
수면－각성 장애 Sleep－Wake Disorders
성기능부전 Sexual Dysfunctions
성별 불쾌감 Gender Dysphoria
파괴적, 충동조절 및 품행 장애 Disruptive, Impulse－Control, and Conduct Disorders
물질관련 및 중독 장애 Substance－Related and Addictive Disorders
신경인지장애 Neurocognitive Disorders
성격장애 Personality Disorders
변태성욕장애 Paraphilic Disorders
기타 정신질환 Other Mental Disorders'''

txt를 읽어 한국어와 영어 명칭을 각각 키와 값으로 갖는 딕셔너리를 생성하는 코드를 작성하세요.

결과
{'신경발달장애': 'Neurodevelopmental Disorders', '조현병 스펙트럼 및 기타 정신병적 장애': 'Schizophrenia Spectrum and Other Psychotic Disorders', 
'양극성 및 관련 장애': 'Bipolar and Related Disorders', '우울장애': 'Depressive Disorders', '불안장애': 'Anxiety Disorder', 
'강박 및 관련 장애': 'Obsessive－Compulsive and Related Disorders', '외상 및 스트레스 관련 장애': 'Trauma－and Stressor－Related Disorders', 
'해리장애': 'Dissociative Disorders', '신체증상 및 관련 장애': 'Somatic Symptom and Related Disorders', '급식 및 섭식장애': 'Feeding and Eating Disorders', 
'배설장애': 'Elimination Disorders', '수면－각성 장애': 'Sleep－Wake Disorders', '성기능부전': 'Sexual Dysfunctions', '성별 불쾌감': 'Gender Dysphoria', 
'파괴적, 충동조절 및 품행 장애': 'Disruptive, Impulse－Control, and Conduct Disorders', '물질관련 및 중독 장애': 'Substance－Related and Addictive Disorders', 
'신경인지장애': 'Neurocognitive Disorders', '성격장애': 'Personality Disorders', '변태성욕장애': 'Paraphilic Disorders', '기타 정신질환': 'Other Mental Disorders'}
"""

if __name__ == '__main__':
    txt = '''신경발달장애 Neurodevelopmental Disorders
조현병 스펙트럼 및 기타 정신병적 장애 Schizophrenia Spectrum and Other Psychotic Disorders
양극성 및 관련 장애 Bipolar and Related Disorders
우울장애 Depressive Disorders
불안장애 Anxiety Disorder
강박 및 관련 장애 Obsessive－Compulsive and Related Disorders
외상 및 스트레스 관련 장애 Trauma－and Stressor－Related Disorders
해리장애 Dissociative Disorders
신체증상 및 관련 장애 Somatic Symptom and Related Disorders
급식 및 섭식장애 Feeding and Eating Disorders
배설장애 Elimination Disorders
수면－각성 장애 Sleep－Wake Disorders
성기능부전 Sexual Dysfunctions
성별 불쾌감 Gender Dysphoria
파괴적, 충동조절 및 품행 장애 Disruptive, Impulse－Control, and Conduct Disorders
물질관련 및 중독 장애 Substance－Related and Addictive Disorders
신경인지장애 Neurocognitive Disorders
성격장애 Personality Disorders
변태성욕장애 Paraphilic Disorders
기타 정신질환 Other Mental Disorders'''

    txt = txt.split('\n')

    dic = {}
    for i in txt:
        count = 0
        while count < len(i) and not(('a' <= i[count] and i[count] <= 'z') or ('A' <= i[count] and i[count] <= 'Z')):
            count += 1
        dic[i[:count - 1]] = i[count:]
    print(dic)

# ord(), chr()를 사용하지 않아도 구현할 수 있음


# txt = '''신경발달장애 Neurodevelopmental Disorders
# 조현병 스펙트럼 및 기타 정신병적 장애 Schizophrenia Spectrum and Other Psychotic Disorders
# 양극성 및 관련 장애 Bipolar and Related Disorders
# 우울장애 Depressive Disorders
# 불안장애 Anxiety Disorder
# 강박 및 관련 장애 Obsessive－Compulsive and Related Disorders
# 외상 및 스트레스 관련 장애 Trauma－and Stressor－Related Disorders
# 해리장애 Dissociative Disorders
# 신체증상 및 관련 장애 Somatic Symptom and Related Disorders
# 급식 및 섭식장애 Feeding and Eating Disorders
# 배설장애 Elimination Disorders
# 수면－각성 장애 Sleep－Wake Disorders
# 성기능부전 Sexual Dysfunctions
# 성별 불쾌감 Gender Dysphoria
# 파괴적, 충동조절 및 품행 장애 Disruptive, Impulse－Control, and Conduct Disorders
# 물질관련 및 중독 장애 Substance－Related and Addictive Disorders
# 신경인지장애 Neurocognitive Disorders
# 성격장애 Personality Disorders
# 변태성욕장애 Paraphilic Disorders
# 기타 정신질환 Other Mental Disorders'''

# disorders = dict()

# is_eng = lambda x: 65 <= ord(x) <= 90 or 97 <= ord(x) <= 122

# for l in txt.split('\n'):
#     i = 0
#     while not is_eng(l[i]):
#         i += 1
#     else:
#         ko, en = l[:i - 1], l[i:]
#         disorders[ko] = en

# print(disorders)

# 해설에선 lambda를 이용해 is_eng 함수를 정의함. 비교문을 여러 개 붙여쓸 수 있다! ('a < b and b < c' 를 'a < b < c'로 표현 가능)