# 모듈

# 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파일이다
# 모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일이라고도 할 수 있다
# 우리는 파이썬으로 프로그래밍을 할 때 굉장히 많은 모듈을 사용한다 다른사람이 만들어 놓은 모듈을 사용할 수도 있고 우리가 직접 만들어서 사용할 수도 있다

# 모듈 만들기
# 모듈에 대해 자세히 살펴보기 전에 간단한 모듈을 한번 만들어보자
# mod1.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b
# 위와 같이 add와 sub함수만 있는 파일 mod1.py를 만들고 /Python/Practice 디렉터리에 저장하자
# 이 mod1.py 파일이 바로 모듈이다 지금까지 에디터로 만들어온 파일과 다르지 않다
# 파이썬 확장자 .py로 만든 파이썬 파일은 모두 모듈이다

# 모듈 불러오기
# 우리가 만든 mod1.py 파일, 즉 모듈을 파이썬에서 불러와 사용하려면 어떻게 해야 할까?
# 먼저 다음과 같이 명령 프롬프트 창을 열고 mod1.py를 저장한 디렉터리로 이동한 다음 대화형 인터프리터를 실행한다
$ cd /Python/Practice
$ python
>>>
# 반드시 mod1.py를 저장한 /Python/Practice 디렉터리로 이동한 다음 예제를 진행해야 한다 그래야만 대화형 인터프리터에서 mod1.py를 읽을 수 있다
import mod1
print(mod1.add(3, 4))
# 7
print(mod1.sub(4, 2))
# 2
# mod1.py를 불러오기 위해 import mod1 이라고 입력하였다 실수로 import mod1.py로 입력하지 않도록 주의하자
# import는 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해주는 명령어이다
# mod1.py 파일에 있는 add 함수를 사용하기 위해서는 위 예와 같이 mod1.add 처럼 모듈 이름 뒤에 "."(도트연산자)를 붙이고 함수 이름을 쓰면 된다
# import는 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있다
# 파이썬 라이브러리는 파이썬을 설치할 떄 자동으로 설치되는 파이썬 모듈을 말한다

# import의 사용 방법은 다음과 같다
import 모듈이름
# 여기에서 모듈이름은 mod1.py에서 .py 확장자를 제거한 mod1만을 가리킨다

# 때로는 mod1.add, mod1.sub처럼 쓰지 않고 add, sub처럼 모듈 이름 없이 함수 이름만 쓰고 싶은 경우도 있을 것이다
# 이럴때는 'from 모듈이름 import 모듈 함수'를 사용하면 된다
from 모듈이름 import 모듈함수
# 위 형식을 사용하면 위와 같이 모듈 이름을 붙이지 않고 바로 해당 모듈의 함수를 쓸 수 있다
from mod1 import add
add(3, 4)
# 7
# 그런데 위와 같이 하면 mod1.py 파일의 add함수만 사용할 수 있다
# add 함수와 sub 함수를 둘 다 사용하고 싶다면 어떻게 해야 할까?
# 2가지 방법이 있다
from mod1 import add, sub
# 첫번째 방법은 위와 같이 'from 모듈 이름 import 모듈함수1, 모듈함수2'처럼 사용하는 것이다 콤마(,)로 구분하여 필요한 함수를 불러올 수 있다
from mod1 import *
# 두 번째 방법은 위와 같이 * 문자를 사용하는 방법이다 정규표현식에서 * 문자는 '모든 것'이라는 뜻인데 파이썬에서도 마찬가지 의미로 사용한다
# 따라서, 'from mod1 import *'는 mod1.py의 모든 함수를 불러서 사용하겠다는 뜻이다

