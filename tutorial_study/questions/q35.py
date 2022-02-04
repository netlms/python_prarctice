"""
ko_en.txt 파일에는 우리말과 영어 문장이 탭으로 구분되어 있습니다.

이 파일을 이용해 영어 퀴즈를 내는 프로그램을 작성하세요. 화면에 우리말로 된 문장을 출력한 다음, 사용자에게 영어 문장을 입력받고, 사용자가 답을 맞혔는지 화면에 표시합니다.

예:

Write the following sentence in English.
그녀는 작가가 아니다.

your answer: She is not a writer.

result: Correct!

--------------------------------------------------------------------------------
Write the following sentence in English.
그들은 교실에 있다.

your answer: They are in the classroom.

result: Correct!

--------------------------------------------------------------------------------
Write the following sentence in English.
너는 집에 있다.

your answer: I am home.

result: Not correct!
right answer:You are home.
"""

from random import *

def make_dic(dic):
    qa = {}
    
    for i in dic[1:]:
        ko, en = tuple(i.split('\t'))
        qa[ko] = en
        
    return (qa)

if __name__ == '__main__':
    f = open('C:\\Users\\MSL\\git\\python_prarctice\\tutorial_study\\questions\\ko_en.txt', encoding='utf8')
    r = f.readlines()
           
    qa = make_dic(r)
    
    num_of_val = len((list(qa.keys())))
    q_num = randrange(0, num_of_val)
    q_statement = (list(qa.keys()))[q_num]
    
    print('Write the following sentence in English.\n' + q_statement + '\n\n' + 'your answer: ', end= '')    
    answer = input()
    print('\nresult: ', end='')
    
    if answer == qa[q_statement].rstrip():
        print('Correct!')
    else:
        print('Not correct!\nright answer: ' + qa[q_statement].rstrip())
    
    
    
# import random

# d = dict()

# with open('ko_en.txt') as f:
#     for line in f.readlines()[1:]:
#         k, v = tuple(line.split('\t'))
#         d[k] = v

# quiz = list(d.keys())
# random.shuffle(quiz)

# while True:
#     if len(quiz) == 0:
#         break
    
#     q = quiz.pop()
#     print("Write the following sentence in English.")
#     print(q)
#     a = input("\nyour answer: ")

#     if a == d[q].rstrip():
#         print('\nresult: Correct!')
#     else:
#         print("\nresult: Not correct!")
#         print("right answer:" + d[q].rstrip() + '\n')

#     input()

#     print('-' * 80)

# 72번째 라인에서 읽어온 문장을 굳이 튜플 타입으로 변환하여 dict에 저장함. 튜플이 리스트보다 더 빠른 속도를 지원한다는 점을 이용한 듯.
# 76번째 라인에서 shuffle()을 이용해 출제하는 문제의 순서를 무작위로 재배열하여 순서대로 출력. 이를 통해 문제가 중복 출제되는 경우를 방지함
# 반복문을 통해 모든 문제를 풀 때까지 문제를 출력하게 함