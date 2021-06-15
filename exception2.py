# 오류 회피하기
# 프로그래밍을 하다보면 특정 오류가 발생할 경우 그냥 통과시켜야 할 때가 있다
try:
    file = open("없는파일", 'r')
except FileNotFoundError:
    pass
# try문 안에서 FileNowFoundError가 발생할 경우에 pass를 사용하여 오류를 그냥 회피하도록 작성한 예제이다



# 오류 일부러 발생시키기
# 이상하게 들리겠지만 프로그래밍을 하다보면 종종 오류를 일부러 발생시켜야 할 경우도 생긴다
# 파이썬은 'raise' 명령어를 사용해 오류를 강제로 발생시킬 수 있다
#
# 예를 들어 Bird 클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 구현하도록 만들고 싶은 경우(강제로 그렇게 하고 싶은 경우)가 있을 수 있다
class Bird:
    def fly(self):
        raise NotImplementedError
# 위 예제는 Bird 클래스를 상속받는 자식클래스는 반드시 fly 함수를 구현해야 한다는 의지를 보여준다
# 만약 자식클래스가 fly 함수를 구현하지 않은 상태로 fly 함수를 호출한다면 어떻게 될까?
# NotImplementedError는 파이썬 내장 오류로 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류를 일으키기 위해 사용한다
class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()
# Traceback (most recent call last):
#  File "...", line 33, in <module>
#   eagle.fly()
#  File "...", line 26, in fly
#   raise NotImplementedError
# NotImplementedError
# Eagle 클래스는 Bird 클래스를 상속받는다 그런데 Eagle 클래스에서 fly 함수를 오버라이딩하지 않았기 때문에 Bird 클래스의 fly 함수가 호출된다
# 그리고 raise 문에 의해 NotImplementedError가 발생할 것이다
# NotImplementedError가 발생되지 않게 하려면 다음과 같이 Eagle 클래스에 fly 함수를 반드시 구현해야 한다
class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()
# 'very fast'



# 에외 만들기
# 프로그램 수행 도중 특수한 경우에만 예외처리를 하기 위해서 종종 예외를 만들어서 사용한다
# 직접 예외를 만들어보자 예외는 다음과 같이 파이썬 내장 클래스인 Exception 클래스를 상속하여 만들 수 있다
class MyError(Exception):
    pass
# 그리고 별명을 출력해 주는 함수를 다음과 같이 작성한다
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
# 그리고 다음과 같이 say_nick 함수를 호출해보자
say_nick("천사")
say_nick("바보")
# 저장한 뒤 프로그램을 실행해보면 다음과 같이 "천사"가 한번 출력된 후 MyError가 발생한다
# 천사
# Traceback (most recent call last):
#  File "...", line 11, in <module>
#   say_nick("바보")
#  File "...", line 7, in say_nick
#   raise MyError()
# __main__.MyError
# 이번에는 예외처리 기법을 사용하여 MyError 발생을 예외처리 해보자
try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다")
# 천사
# 허용되지 않는 별명입니다
# 만약 오류메세지를 사용하고 싶다면 다음처럼 예외처리를 하면 된다
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
# 천사
#
# 하지만 프로그램을 실행해 보면 print(e)로 오류메세지가 출력되지 않는 것을 확인할 수 있다
# 오류메세지를 출력했을때 오류메세지가 보이게 하려면 오류 클래스에 다음과 같은 __str__ 메서드를 구현해야 한다
# __str__ 메서드는 print(e)처럼 오류 메세지를 print문으로 출력할 경우에 호출되는 메서드이다
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다"
# 천사
# '허용되지 않는 별명입니다'
# 프로그램을 다시 실행해보면 "허용되지 않는 별명입니다"라는 오류메세지가 출력되는 것을 확인할 수 있다

