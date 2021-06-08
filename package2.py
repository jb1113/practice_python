# relative 패키지

# 만약 graphic 디렉터리의 render.py 모듈이 sound 디렉터리의 echo.py 모듈을 사용하고 싶다면 어떻게 해야 할까?
# 다음과 같이 render.py를 수정하면 가능하다
# render.py
from game.sound.echo import echo_test
def render_test():
    print("render")
    echo_test()
# from game.sound.echo import echo_test 문장을 추가하여 echo_test 함수를 사용할 수 있도록 수정했다
from game.graphic.render import render_test
render_test()
# render
# echo
# 위 예제처럼 from game.sound.echo import echo_test를 입력해 전체 경로를 사용하여 import 할 수도 있지만 다음과 같이 relative하게 import하는것도 가능하다
# render.py
from ..sound.echo import echo_test
def render_test():
    print("render")
    echo_test()
# from game.sound.echo import echo_test가 from ..sound.echo import echo_test로 변경되었다
# 여기에서 ..은 상위 디렉터리를 의미한다
# graphic과 sound디렉터리는 동일한 깊이(depth)이므로 상위 디렉터리(..)을 사용하여 위와 같은 import가 가능한 것이다

# relative한 접근자에는 다음과 같은 것이 있다
# .. - 상위 디렉터리
# .  - 현재 디렉터리
# .. 과 같은 relative한 접근자는 render.py처럼 모듈 안에서만 사용해야 한다
# 파이썬 인터프리터에서 relative한 접근자를 사용하면 "SystemError: cannot perform relative import" 오류가 발생한다

