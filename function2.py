# 매개변수 지정하여 호출하기
# 함수를 호출할 때 매개변수를 지정할 수 있다
def add(a, b):
    return a+b
# 위 함수를 매개변수를 지정하여 사용하면
result = add(a=3, b=7)  # a에 3, b에 7을 전달
print(result)
# 10
# 매개변수를 지정하면 다음과 같이 순서에 상관없이 사용할 수 있다
result = add(b=7, a=3)  # b에 7, a에 3을 전달
print(result)
# 10

# 입력값이 몇개가 될지 모를경우에는 어떻게 해야하나?
# 입력값이 여러개일때 그 입력값을 모두 더해주는 함수를 생각해보자
def 함수이름(*매개변수):
    수행할문장1
    ...
# 일반적으로 볼 수 있는 함수형태의 괄호 안 매개변수 부분이 *매개변수로 바뀌었다

# 여러개의 입력값을 받는 함수 만들기
def add_many(*args):
    result = 0
    for i in args:
        result = result + i

    return result

result = add_many(1, 2)
print(result)
# 3
result = add_many(1, 2, 3)
print(result)
# 6
result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)
# 55

# 위에서 만든 add_many 함수는 입력값이 몇개든 상관이 없다
# *args처럼 매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아서 튜플로 만들어주기 때문이다
# 만약 add_many(1, 2, 3)처럼 이 함수를 사용하면 args는 (1, 2, 3)이 된다

# 여러개의 입력을 처리할때 def add_many(*args)처럼 함수의 매개변수로 *args만 사용할 수 있는것은 아니다
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i

    return result
# add_mul 함수는 여러 개의 입력값을 의미하는 *args 매개변수 앞에 choice 매개변수가 추가되었다
# 이는 다음과 같이 사용할 수 있다
result = add_mul('add', 1, 2, 3, 4, 5)
print(result)
# 15
result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)
# 120
# 매개변수 choice에 'add'가 입력된 경우 *args에 입력되는 모든 값을 더하고 'mul'이 입력된 경우 모든 값을 곱한다

# 키워드 파라미터 (kwargs)
# 키워드 파라미터를 사용할 때는 매개변수 앞에 별 두개(**)를 붙인다
def print_kwargs(**kwargs):
    print(kwargs)
# print_kwargs 함수는 매개변수 kwargs를 출력하는 함수이다
print_kwargs(a=1)
# {'a' : 1}
print_kwargs(name='foo', age=3)
# {'age' : 3, 'name' : 'foo'}
#
# 입력값 a=1 또는 name='foo', age=3이 모두 딕셔너리로 만들어져서 출력된다는 것을 확인할 수 있다
# 즉 **kwargs처럼 매개변수 이름 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고
# 모든 key=value 형태의 결과값이 그 딕셔너리에 저장된다
# 여기에서 kwargs는 keyword arguments의 약자이며 args와 마찬가지로 관례적으로 사용한다

# 함수의 결과값은 언제나 하나이다
def add_and_mul(a, b):
    return a+b, a*b
# add_and_mul 함수는 2개의 입력 인수를 받아 더한 값과 곱한 값을 돌려주는 함수이다
# 이 함수를 다음과 같이 호출하면 어떻게 될까?
result = add_and_mul(3, 4)
# 결과값은 a+b와 a*b 2개인데 결과값을 받아들이는 변수는 result 하나만 쓰였으니 오류가 발생하지 않을까?
# 하지만 오류는 발생하지 않는다
# 그 이유는 함수의 결과값은 2개가 아니라 언제나 1개라는 데 있다
# add_and_mul 함수와 결과값 a+b와 a*b는 튜플값 하나인 (a+b, a*b)로 돌려준다
# 따라서 result 변수는 다음과 같은 값을 갖는다
result = (7, 12)    # 두 개의 값을 가진 하나의 튜플
# 만약 이 하나의 튜플값을 2개의 결과값처럼 받고 싶다면 다음과 같이 함수를 호출한다
result1, result2 = add_and_mul(3, 4)
# result1, result2 = (7, 12)
# 이렇게 호출하면 result1, result2 = (7, 12)가 되어 result1은 7이 되고 result2는 12가 된다

# 다음과 같은 의문이 생길 수도 있다
def add_and_mul(a, b):
    return a+b
    return a*b
# 위와 같이 return문을 2번 사용하면 2개의 결과값을 돌려주지 않을까?
# 하지만 파이썬에서 위와 같은 함수는 참 어리석은 함수이다
# 이유는 add_and_mul 함수를 호출해보면 알 수 있다
result = add_and_mul(2, 3)
print(result)
# 5
# add_and_mul(2, 3)의 결과값은 5 하나뿐이다 두번째 return문인 return a*b는 실행되지 않았다는 뜻이다
# 따라서 이 함수는 다음과 완전히 동일하다
def add_and_mul(a, b):
    return a+b
# 즉 함수는 return문을 만나는 순간 결과값을 돌려준 다음 함수를 빠져나간다

# return의 또다른 쓰임새
# 특별한 상황일 때 함수를 빠져나가고 싶다면 return을 단독으로 써서 함수를 즉시 빠져나갈수 있다
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다" % nick)
# 위 함수는 별명을 입력으로 전달받아 출력하는 함수이다 이 함수 역시 반환값(결과값)은 없다
# (문자열을 출력한다는 것과 반환값이 있다는 것은 전혀 다른 말이다 혼동하지 말자)
# 함수의 반환값은 오로지 return문에 의해서만 생성된다
# 만약에 입력값으로 '바보'라는 값이 들어오면 문자열을 출력하지 않고 함수를 즉시 빠져나간다
say_nick('야호')
# 나의 별명은 야호입니다
say_nick('바보')
#
# 이처럼 return으로 함수를 빠져나가는 방법은 실제 프로그래밍에서 자주 쓰인다

# 매개변수에 초기값 미리 설정하기
def say_myself(name, age, man=True):
    print("나의 이름은 %s 입니다" % name)
    print("나이는 %d살 입니다" % age)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")
# 위 함수를 보면 매개변수가 name, age, man=True 이렇게 3개가 있다
# man=True처럼 매개변수에 미리 값을 넣어준 것이다
# 이것이 바로 함수의 매개변수 초기값을 설정하는 방법이다
# 함수의 매개변수에 들어갈 값이 항상 변하는 것이 아닐 경우에는 이렇게 함수의 초기값을 미리 설정해두면 유용하다
#
# 위 함수는 다음처럼 사용할 수 있다
say_myself("JB", 30)
say_myself("JB", 30, True)
say_myself("JB", 30, False)

# 함수의 매개변수에 초기값을 설정할 때 주의할 것이 있다 만약 위의 함수를 다음과 같이 만들면
def say_myself(name, man=True, age):
    print("나의 이름은 %s 입니다" % name)
    print("나이는 %d살 입니다" % age)
    ...
# 이전 함수와 바뀐 부분은 초기값을 설정한 매개변수의 위치이다
# 결론부터 말하면 이 함수를 실행할 때 오류가 발생한다
# 다음과 같이 호출했다고 생각해보자
say_myself("JB", 30)
# 위와 같이 호출한다면 name 변수에는 "JB"이 들어갈 것이다
# 하지만 파이썬 인터프리터는 30을 man 변수와 age 변수중 어느 곳에 대입해야 할지 알 수 없게된다
# 오류 메세지를 보면 다음과 같다
SyntaxError: non-default argument follows default argument
# 위 오류 메세지는 초기값을 설정해 놓은 매개변수 뒤에 초기값을 설정해 놓지않은 매개변수는 사용할 수 없다는 뜻이다
# 초기화시키고 싶은 매개변수를 항상 뒤쪽에 놓아야 한다

# 함수 안에서 선언한 변수의 효력 범위
# 함수 안에서 사용할 변수의 이름을 함수 밖에서도 동일하게 사용한다면 어떻게 될까?
number = 1
def varscope(number):
    number = number + 1

varscope(number)
print(number)
# 1
# 2를 예상했지만 아닌이유는?
# 함수안에서 새로만든 매개변수는 함수 안에서만 사용하는 함수만의 변수이기 때문이다
# 즉 def varscope(number)에서 입력값을 전달받는 매개변수 number는 함수 안에서만 사용하는 변수이지
# 함수 밖의 변수 number가 아니라는 뜻이다

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 그렇다면 위의 varscope라는 함수를 사용해서 함수 밖의 변수 number를 1만큼 증가시킬수 있는 방법은 없을까?
# 1. return 사용하기
number = 1
def varscope(number):
    number = number + 1
    return number

number = varscope(number)
print(number)
# 2

# 2. global 명령어 사용하기
number = 1
def varscope():
    global number
    number = number + 1

varscope()
print(number)
# 2
# 위와 같이 varscope함수 안의 global number 문장은 함수 안에서 함수 밖의 number 변수를 직접 사용하겠다는 뜻이다
# 하지만 프로그래밍을 할 때 global 명령어는 사용하지 않는 것이 좋다
# 왜냐하면 함수는 독립적으로 존재하는 것이 좋기 떄문이다
# 외부변수에 종속적인 함수는 그다지 좋은 함수가 아니다 그러므로 가급적 이 방법은 피하도록 한다



# lambda
# lambda는 함수를 생설할 떄 사용하는 예약어로 def와 동일한 역할을 한다
# 보통 함수를 한줄로 간결하게 만들 때 사용한다 우리말로는 "람다"라고 읽고
# def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다
# 사용법은 다음과 같다
lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식

add = lambda a, b : a+b
result = add(3, 4)
print(result)
# 7
# add는 두개의 인수를 받아 서로 더한 값을 돌려주는 lambda 함수이다
# 위 예제는 def를 사용한 다음 함수와 하는 일이 완전히 동일하다
def add(a, b):
    return a+b

result = add(3, 4)
print(result)
# 7
# lambda 예약어로 만든 함수는 return 명령어가 없어도 결과값을 돌려준다

