"""
korean_national_anthem_1.txt 파일에는 애국가 1절 가사가 있습니다.

동해 물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세.
무궁화 삼천리 화려 강산
대한 사람, 대한으로 길이 보전하세.

마찬가지로 4절까지의 가사가 텍스트 파일에 나뉘어 저장되어 있습니다.

korean_national_anthem_2.txt
korean_national_anthem_3.txt
korean_national_anthem_4.txt

이 파일들을 읽어 out.txt 파일에 다음과 같이 저장하는 파이썬 스크립트를 작성하세요.

korean_national_anthem_1.txt
----------------------------
동해 물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세.
무궁화 삼천리 화려 강산
대한 사람, 대한으로 길이 보전하세.

korean_national_anthem_2.txt
----------------------------
남산 위에 저 소나무, 철갑을 두른 듯
바람 서리 불변함은 우리 기상일세.
무궁화 삼천리 화려 강산
대한 사람, 대한으로 길이 보전하세.

korean_national_anthem_3.txt
----------------------------
가을 하늘 공활한데 높고 구름 없이
밝은 달은 우리 가슴 일편단심일세.
무궁화 삼천리 화려 강산
대한 사람, 대한으로 길이 보전하세.

korean_national_anthem_4.txt
----------------------------
이 기상과 이 맘으로 충성을 다하여
괴로우나 즐거우나 나라 사랑하세.
무궁화 삼천리 화려 강산
대한 사람, 대한으로 길이 보전하세.
"""

if __name__ == '__main__':
    
    anthem = {}
    f_name = []
    
    for i in range(4):
        # print(i)
        f = (open('.\\tutorial_study\\questions\\korean_national_anthem_' + str(i + 1) + '.txt'))
        f_name.append('korean_national_anthem_' + str(i + 1) + '.txt')
        anthem[f_name[i]] = f.read()
    
    w = open('.\\tutorial_study\\questions\\out.txt', 'w')
    
    for i in range(4):
        w.write(f_name[i])
        w.write('\n----------------------------\n')
        w.write(anthem[f_name[i]])
        w.write('\n\n')
    
    w.close()
    
    f = open('.\\tutorial_study\\questions\\out.txt')
    
    print(f.read())
    
#     import glob

# outfile = open("out.txt", "wt")

# for x in glob.glob("korean_national_anthem_?.txt"):
#     infile = open(x, "rt")
#     #infile = open(x, "rt", encoding="utf-8-sig")
    
#     outfile.write(x + '\n')
#     outfile.write('-' * len(x) + '\n')
#     outfile.write(infile.read() + "\n\n")

# outfile.close()

# glob 모듈을 사용해 파일명을 더 효율적으로 가져와 처리함. glob을 통한 정규식 이용에 익숙해질 필요가 있음