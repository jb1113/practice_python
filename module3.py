# 클래스나 변수 등을 포함한 모듈

# 지금까지 살펴본 모듈은 함수만 포함했지만 클래스나 변수 등을 포함할 수도 있다
# mod2.py
PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)

def add(a, b):
    return a + b
# 이 파일은 원의 넓이를 계산하는 Math 클래스와 두 값을 더하는 add 함수 그리고 원주율 값에 해당되는 PI 변수처럼 클래스, 함수, 변수 등을 모두 포함하고 있다
# 대화형 인터프리터를 열고 다음과 같이 따라해보자
$ python
>>> import mod2
>>> print(mod2.PI)
# 3.141592
# 위 예에서 볼 수 있듯이 mod2.PI 처럼 입력해서 mod2 파일에 있는 PI 변수 값을 사용할 수 있다
math = mod2.Math()
print(math.solv(2))
# 12.566368
# 위 예에서는 mod2.py에 있는 Math 클래스를 사용하는 방법을 보여준다
# 위 예처럼 모듈 안에 있는 클래스를 사용하려면 "."(도트 연산자)로 클래스 이름 앞에 모듈 이름을 먼저 입력해야 한다
print(mod2.add(mod2.PI, 4.4))
# 7.5415920000000005
# mod2.py에 있는 add 함수 역시 당연히 사용할 수 있다



# 다른 파일에서 모듈 불러오기
# 지금까지는 만들어 놓은 모듈 파일을 사용하기 위해 대화형 인터프리터만 사용했다
# 이번에는 다른 파이썬 파일에서 이전에 만들어 놓은 모듈을 불러와서 사용하는 방법에 대해 알아보자
# modtest.py
import mod2
result = mod2.add(3, 4)
print(result)
# 위에서 볼 수 있듯이 다른 파이썬 파일에서도 import mod2로 mod2 모듈을 불러와서 사용할 수 있다
# 대화형 인터프리터에서 한 것과 마찬가지 방법이다
# 위 예제가 정상적으로 실행되기 위해서는 modtest.py 파일과 mod2.py 파일이 동일한 디렉터리(/Python/Practice)에 있어야 한다

# 모듈을 불러오는 또 다른 방법
# 우리는 지금껏 명령 프롬프트 창을 열고 모듈이 있는 디렉터리로 이동한 다음에 모듈을 사용할 수 있었다
# 이번에는 모듈을 저장한 디렉터리로 이동하지 않고 모듈을 불러와서 사용하는 방법에 대해 알아보자
# 먼저 다음과 같이 이전에 만든 mod2.py 파일을 /Python/Practice/mod/ 로 이동시킨다
mkdir mod
mv ./mod2.py ./mod/mod2.py
# 그리고 다음 예를 따라해보자

# 1. sys.path.append('모듈을 저장한 디렉터리') 사용하기
# 먼저 sys 모듈을 불러온다
>>> import sys
# sys 모듈은 파이썬을 설치할 때 함께 설치되는 라이브러리 모듈이다
# sys 모듈을 사용하면 파이썬 라이브러리가 설치되어 있는 디렉터리를 확인할 수 있다
# 다음과 같이 입력해보자
sys.path
# ['', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']
# sys.path는 파이썬 라이브러리가 설치되어 있는 디렉터리를 보여준다
# 만약 파이썬 모듈이 위 디렉터리에 들어 있다면 모듈이 저장된 디렉터리로 이동할 필요 없이 바로 불러서 사용할 수 있다
# 그렇다면 sys.path에 /Python/Practice/mod/ 디렉터리를 추가하면 아무 곳에서나 불러 사용할 수 있지 않을까?
# 명령 프롬프트 창에서는 /, \ 든 상관없지만 소스 코드 안에서는 반드시 / 또는 \\ 기호를 사용해야 한다

# 당연히 sys.path의 결과값이 리스트이므로 우리는 다음과 같이 할 수 있다
sys.path.append("/Python/Practice/mod")
sys.path
# ['', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages', '/Users/a201903165/Python/Practice/mod']
# sys.path.append를 사용해서 '/Python/Practice/mod'라는 디렉터리를 sys.path에 추가한 후 다시 sys.path를 보면
# 가장 마지막 요소에 '/Python/Practice/mod'라고 추가된 것을 확인할 수 있다
# 실제로 모듈을 불러와서 사용할 수 있는지 확인해보자
import mod2
print(mod2.add(3, 4))
# 7
# 이상없이 불러와서 사용할 수 있다

# 2. PYTHONPATH 환경 변수 사용하기
# 모듈을 불러와서 사용하는 또 다른 방법으로는 PYTHONPATH 환경 변수를 사용하는 방법이 있다
# 다음과 같이 입력해보자
$ export PYTHONPATH=/Users/a201903165/Python/Practice/mod
$ python
>>> import mod2
>>> print(mod2.add(3, 4))
# 7
# export 명령어를 사용해 PYTHONPATH 환경 변수에 mod2.py 파일이 있는 디렉터리를 설정한다
# 그러면 디렉터리 이동이나 별도의 모듈 추가 작업 없이 mod2 모듈을 불러와서 사용할 수 있다

