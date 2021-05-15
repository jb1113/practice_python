# 함수
# 함수란 무엇인가?
# 입력값을 가지고 어떠한 일을 수행한 다음에 그 결과값을 출력하는것
# 반복적인 부분을 한 묶음으로 묶어 어떤 입력값이 주어졌을 때 어떤 결과값을 돌려주는 함수로 작성

# 파이썬 함수의 구조
def 함수명(매개변수):
    수행할 문장1
    수행할 문장2
    ...
# def 키워드를 사용하여 함수를 만든다
def add(a, b):
    return a + b
# 함수의 이름은 add이고 입력으로 2개의 값을 받고 2개의 값을 합한 결과를 반환한다

# 매개변수와 인수
# 매개변수(parameter)와 인수(arguments)는 혼용해서 사용되는 헷갈리는 용어이므로 잘 기억해두자
# 매개변수는 함수에 입력으로 전달된 값을 받는 변수를 의미하고
# 인수는 함수를 호출할 때 전달하는 입력값을 의미한다
def add(a, b):      # a, b는 매개변수
    return a + b

print(add(1, 2))    # 1, 2는 인수

# 입력값과 결과값에 따른 함수의 형태
# 입력값 -> 함수 -> 결과값
# 1. 입력값이 있고 결과값이 있는 함수 (일반적인 함수)
def 함수이름(매개변수):
    수행할 문장
    ...
    return 결과값

def add(a, b):
    result = a + b
    return result

result = add(1, 2)
print(result)
# 3
#
# 결과값을받을변수 = 함수이름(인수1, 인수2, ...)

# 2. 입력값이 없는 함수
def 함수이름():
    수행할 문장
    ...
    return 결과값

def say():
    return 'Hello'

result = say()
print(result)
# 'Hello'
#
# 결과값을받을변수 = 함수이름()

# 3. 결과값이 없는 함수
def 함수이름():
    수행할 문장
    ...

def add(a, b):
    print("%d과 %d의 합은 %d입니다" % (a, b, a+b))

add(1, 2)
# 1과 2의 합은 3입니다
#
# 함수이름(인수1, 인수2, ...)

# 위 문장을 출력해 주었는데 왜 결과값이 없다는 것인지 의아하게 생각할 수 있다
# print문은 함수의 구성 요소 중 하나인 수행할 문장에 해당하는 부분이다
# 결과값은 오로지 return 명령으로만 돌려받을수 있다
# 이를 확인 하기 위하여
result = add(1, 2)
print(result)
# None
# 위와 같이 result 변수에 대입하여 출력해보면 결과값은 None이다

# 4. 입력값도 결과값도 없는 함수
def 함수이름():
    수행할문장
    ...

def say():
    print("Hello")

say()
# 'Hello'
#
# 함수이름()
