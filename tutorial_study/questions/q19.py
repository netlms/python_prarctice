"""
문자열을 슬라이싱 해서, 문자열에 속한 문자들을 거꾸로 배열한 문자열을 얻을 수 있습니다.
>>> 'Python'[::-1]
'nohtyP'

문자열의 lower() 메서드를 이용해 소문자만으로 이루어진 문자열을 얻을 수 있습니다.
>>> 'Python'.lower()
'python'

그리고 replace() 메서드를 이용해 문자열 일부를 다른 문자열로 바꾼 문자열을 얻을 수 있습니다.
>>> 'Python'.replace('P', 'J')
'Jython'

문제

거꾸로 배열해도 같은 단어 혹은 문장이 되는 것을 회문(palindrome)이라고 합니다. 다음은 회문의 예입니다.

Anna
Civic
Kayak
Level
...

문제 1

주어진 단어가 회문인지 판별하는 함수 palindrome()을 작성하세요. 단, 문자열 입력은 모두 소문자로 이뤄지며 공백을 포함하지 않는다고 가정합니다.

>>> palindrome('anna')
True
>>> palindrome('banana')
False

문제 2

대문자와 소문자가 섞여 있더라도 회문으로 판정하도록 함수를 개선하세요.

>>> palindrome('Anna')
True

문제 3

공백이 섞여 있더라도 회문으로 판정하도록 함수를 개선하세요.

>>> palindrome('My gym')
True
"""

# Q1
def palindrome(str):
    front = str[:len(str) // 2]
    back = str[::-1][:len(str) // 2]
    if front == back:
        return True
    else:
        return False

print(palindrome(input()))


# Q2
def palindrome(str):
    front = str[:len(str) // 2].lower()
    back = str[::-1][:len(str) // 2].lower()
    if front == back:
        return True
    else:
        return False

print(palindrome(input()))


# Q3
def palindrome(str):
    rm_blank = str.replace(' ', '')
    front = rm_blank[:len(rm_blank) // 2].lower()
    back = rm_blank[::-1][:len(rm_blank) // 2].lower()
    if front == back:
        return True
    else:
        return False

print(palindrome(input()))




# def palindrome(s):
#     s = s.lower()
#     s = s.replace(' ', '')
#     return s[:] == s[::-1]

# if __name__ == '__main__':
#     for x in ['anna', 'banana', 'Anna', 'My gym']:
#         if palindrome(x):
#             print(f"'{x}' is a panlindrome")
#         else:
#             print(f"'{x}' is not a palindrome")