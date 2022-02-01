"""
농구팀에 속한 12명의 득점을 다음과 같이 score 리스트로 나타냈습니다.
>>> score = [0, 0, 2, 4, 7, 7, 9]
>>> score += [11, 11, 13, 18]
>>> score += [20]
>>> score
[0, 0, 2, 4, 7, 7, 9, 11, 11, 13, 18, 20]

다음과 같이 stem_leaf 리스트를 만들어 선수들의 득점을 줄기와 잎 그림 형식으로 저장하려고합니다.
>>> stem_leaf = [[], [], []]

문제 1

stem_leaf에 데이터를 채우는 프로그램을 작성하세요. 데이터가 채워진 결과는 다음과 같습니다.
>>> stem_leaf
[[0, 0, 2, 4, 7, 7, 9], [1, 1, 3, 8], [0]]
>>> stem_leaf[0]
[0, 0, 2, 4, 7, 7, 9]
>>> stem_leaf[1]
[1, 1, 3, 8]
>>> stem_leaf[2]
[0]

문제 2

stem_leaf를 다음과 같은 형태로 프린트하는 프로그램을 작성하세요.
0: [0, 0, 2, 4, 7, 7, 9]
1: [1, 1, 3, 8]
2: [0]
"""

score = [0, 0, 2, 4, 7, 7, 9, 11, 11, 13, 18, 20]
stem_leaf = [[],[],[]]

for i in score:
        stem_leaf[i // 10].append(i % 10)

print(stem_leaf, '\n')

count = 0

for i in stem_leaf:
    print(f'{count}: {i}')

# score = [0, 0, 2, 4, 7, 7, 9]
# score += [11, 11, 13, 18]
# score += [20]

# stem_leaf = [[], [], []]

# # ex 1

# for s in score:
#     d, m = divmod(s, 10)
#     stem_leaf[d].append(m)

# # ex 2

# for i in range(len(stem_leaf)):
#     print(f'{i}: {stem_leaf[i]}')