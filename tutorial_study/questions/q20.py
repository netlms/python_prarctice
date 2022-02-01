"""
정수 num을 매개변수로 받아 각 자리 숫자(digit)의 합을 계산하는 sumOfDigits() 함수를 작성하세요. 단, 나눗셈을 이용하지 말고 풀어보세요.
"""

def sumOfDigits(num):
    digit = list(str(num))
    sum = 0
    for i in digit:
        sum += int(i)
    
    return (sum)

print(sumOfDigits(1234))
print(sumOfDigits(643))
print(sumOfDigits(47253))

# def sumOfDigits(num):
#     sum = 0
#     for c in list(str(num)):
#         sum += int(c)

#     return sum

# if __name__ == '__main__':
#     print(sumOfDigits(47253))
#     print(sumOfDigits(643))