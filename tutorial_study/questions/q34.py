"""
제2차 세계대전이 한창이던 1943년 미국 로스앤젤레스의 집배원은 엽서 한 장을 집어들었습니다. 
보낸이는 일본의 전쟁포로 수용소에 수감돼 있던 미군 프랭크 조넬리스, 받는이는 페더럴 빌딩 회사 1619호의 F.B.Iers 씨로 적혀 있었습니다. 
회사도 사람도 실제로 존재하지 않았지만, 해당 주소의 619호에는 연방수사국(FBI) 사무실이 있었습니다.

엽서의 내용은 다음과 같습니다.


                August 29, 1943
Dear Iers:

After surrender, health improved
fifty percent.  Better food etc.
Americans lost confidence
in Philippines.  Am comfortable
in Nippon.  Mother: Invest
30%, salary, in business.  Love

                (signed)
                Frank G. Jonelis
                
"항복 후, 건강이 50% 나아졌다. 좋은 음식 등. 미국인은 필리핀에서 자신감을 잃었다. 일본에서 편안하다. 어머니: 30% 투자, 봉급, 사업에. 사랑해"

문장이 약간 어색하긴 했지만 별다른 내용이 없어 보였습니다. 
그렇지만 연방수사국에서는 여기에 다른 메시지가 숨겨져 있을지 모른다고 생각해 여러 가지 방법으로 단어를 배열해보다가, 
각 줄의 첫 두 단어를 문장 부호 없이 조합하면 다음의 문장을 만들 수 있다는 것을 알아냈습니다.(마지막 단어 생략)

AFTER SURRENDER FIFTY PERCENT AMERICANS LOST IN PHILIPPINES IN NIPPON 30%
"항복한 후 필리핀에서 50% 일본에서 30%의 미군을 잃었다"

문제
텍스트 편집기를 사용해 위의 엽서 내용을 postcard.txt 파일에 저장합니다.

1. 파일 읽기
postcard.txt 파일을 읽어 화면에 출력하세요.

2. 본문 추려내기
엽서 내용은 머리말, 본문, 꼬리말 형태로 되어 있고 그 사이는 한 줄 씩 띄어져 있습니다. 본문 내용만 화면에 출력하세요.

출력
After surrender, health improved
fifty percent.  Better food etc.
Americans lost confidence
in Philippines.  Am comfortable
in Nippon.  Mother: Invest
30%, salary, in business.  Love

3. 문장부호 제거
본문에서 마침표(.), 쉼표(,), 콜론(:)을 제거해 출력하세요.

출력
After surrender health improved
fifty percent  Better food etc
Americans lost confidence
in Philippines  Am comfortable
in Nippon  Mother Invest
30% salary in business  Love

4. 대문자로 변환
3번의 출력 결과를 모두 대문자로 나타내세요.

출력
AFTER SURRENDER HEALTH IMPROVED
FIFTY PERCENT  BETTER FOOD ETC
AMERICANS LOST CONFIDENCE
IN PHILIPPINES  AM COMFORTABLE
IN NIPPON  MOTHER INVEST
30% SALARY IN BUSINESS  LOVE

5. 비밀 메시지 출력
4번의 결과에서 각 행의 처음 두 단어만 추려서 출력하세요.

AFTER SURRENDER FIFTY PERCENT AMERICANS LOST IN PHILIPPINES IN NIPPON 30% SALARY
"""

if __name__ == "__main__":
    
    # write text to the file
    f = open('.\\tutorial_study\\questions\\postcard.txt', 'w')
    f.write('                August 29, 1943\nDear Iers:\n\nAfter surrender, health improved\nfifty percent.  Better food etc. \
            \nAmericans lost confidence\nin Philippines.  Am comfortable\nin Nippon.  Mother: Invest \
            \n30%, salary, in business.  Love\n\n                (signed)\n                Frank G. Jonelis)')
    f. close()
    
    f = open('.\\tutorial_study\\questions\\postcard.txt')
    r = f.read()
    print(r, '\n')
    
    f.seek(0)
    
    # get body from the text
    line = f.readlines()
    
    body_start = 0
    body_end = 0
    count = 0
    for i in line:
        if i == '\n':
            if body_start == 0:
                body_start = count
            else:
                body_end = count
                break
        count += 1
    
    body = line[body_start + 1:body_end]
    
    index = 0
    for sentence in body:
        sentence = sentence.rstrip('\n')
        body[index] = sentence
        print(sentence)   
        index += 1
        
    print()
    
    # remove '.', ',', ':' from the body
    index = 0
    for sentence in body:
        sentence = sentence.replace('.','')
        sentence = sentence.replace(',','')
        sentence = sentence.replace(':','')
        body[index] = sentence
        print(body[index])
        index += 1

    print()
    
    # change all letters to capital
    index = 0
    for sentence in body:
        sentence = sentence.upper()
        body[index] = sentence
        print(body[index])
        index += 1
    
    print()
    
    # get first two words from each sentence
    index = 0
    for sentence in body:
        two_words = sentence.split()
        
        print(two_words[0], two_words[1], '', end='')
        
        
        
#  # 1
# txt = open("postcard.txt", "r").read()
# print("*** 1. Full Text ***\n" + txt + '\n')

# # 2
# head, body, tail = tuple(txt.split('\n\n'))
# print("*** 2. Body ***\n" + body + '\n')

# # 3
# import re
# s = re.sub('[:,\.]', '', body)
# print("*** 3. Text without Punctuation ***\n" + s + '\n')

# # 4
# s = s.upper()
# print("*** 4. Uppercase ***\n" + s + '\n')

# # 5
# secret_words = []
# for line in s.split('\n'):
#     secret_words += line.split()[:2]

# message = ' '.join(secret_words)
# print("*** 5. Secret Message ***\n" + message)

# 해설에서는 튜플, re 모듈, 식 표현 등을 유연하게 사용하여 간결하게 표현함. 자연스럽게 활용하기 위해 많은 실습이 필요.