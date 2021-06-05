# if __name__ == "__main__": 의 의미

# 이번에는 mod1.py 파일을 다음과 같이 변경해보자
# mod1.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print(add(1, 4))
print(sub(4, 2))
# add(1, 4)와 sub(4, 2)의 결과를 출력하는 다음 문장을 추가하였다
# 위에서 작성한 mod1.py 파일은 다음과 같이 실행할 수 있다
python mod1.py
# 5
# 2
# 그런데 이 mod1.py 파일의 add와 sub 함수를 사용하기 위해 mod1 모듈을 import할 때는 좀 이상한 문제가 생긴다
# 명령 프롬프트 창에서 다음을 따라해보자
$ python
>>> import mod1
# 5
# 2
# 엉뚱하게도 import mod1을 수행하는 순간 mod1.py가 실행이 되어 결과값을 출력한다
# 우리는 단지 mod1.py 파일의 add와 sub함수만 사용하려고 했는데 말이다
# 이러한 문제를 방지하려면 mod1.py 파일을 다음과 같이 변경해야 한다
# mod1.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
# if __name__ == "__main__" 을 사용하면 '$ python mod1.py' 처럼 직접 이 파일을 실행했을 때는 '__name__ == "__main__"'이 참이 되어 if문 다음 문장이 수행된다
# 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는 '__name__ == "__main__"'이 거짓이 되어 if문 다음 문장이 수행되지 않는다
# 위와 같이 수정한 후 다시 대화형 인터프리터를 열고 실행해보자
$ python
>>> import mod1
>>>
# 아무 결과값도 출력되지 않는 것을 확인할 수 있다

# __name__ 변수란?
# 파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다
# 만약 '$ python mod1.py'처럼 직접 mod1.py 파일을 실행할 경우 mod1.py의 __name__ 변수에는 __main__ 값이 저장된다
# 하지만 파이썬 쉘이나 다른 파이썬 모듈에서 mod1을 import할 경우에는 mod1.py의 __name__ 변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다

