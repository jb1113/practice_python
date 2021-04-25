# 불 자료형

# 불 자료형이란?
# 불(bool) 자료형이란 참(True)과 거짓(False)을 나타내는 자료형이다 불 자료형은 다음 2가지 값만을 가질 수 있다
# True - 참
# False - 거짓
# True나 False는 파이썬의 예약어로 true, false와 같이 사용하지 말고 첫 문자를 항상 대문자로 사용해야 한다

a = True
b = False
# 따옴표로 감싸지 않은 문자열을 변수에 지정해서 오류가 발생할 것 같지만 잘 실행된다
# type 함수를 변수 a와 b에 사용하면 두 변수의 자료형이 bool로 지정된 것을 확인할 수 있다
type(a)
# <class 'bool'>
type(b)
# <class 'bool'>
# type(x)는 x의 자료형을 확인하는 파이썬의 내장 함수이다



# 자료형의 참과 거짓
# 자료형에 참과 거짓이 있다 이는 매우 중요한 특징이며 실제로도 자주 쓰인다
# 값        | 참 or 거짓
# "python"  | 참
# ""        | 거짓
# [1, 2, 3] | 참
# []        | 거짓
# ()        | 거짓
# {}        | 거짓
# 1         | 참
# 0         | 거짓
# None      | 거짓
#
# 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있으면 ("", [], (), {}) 거짓이 된다 당연히 비어있지 않으면 참이 된다
# 숫자에서는 그 값이 0일 때 거짓이 된다

a = [1, 2, 3, 4]
while a:
    print(a.pop())
# 4
# 3
# 2
# 1

if []:
    print("참")
else:
    print("거짓")
# 거짓

if [1, 2, 3]:
    print("참")
else:
    print("거짓")
# 참

# 불 연산
# bool 내장 함수를 사용하면 자료형의 참과 거짓을 식별할 수 있다
bool('python')
# True
bool('')
# False
bool([1, 2, 3])
# True
bool([])
# False
bool(0)
# False
bool(3)
# True

