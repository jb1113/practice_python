# 클래스

# 클래스는 왜 필요한가?
# 클래스는 지금까지 공부한 함수나 자료형처럼 프로그램 작성을 위해 꼭 필요한 요소는 아니다
# 하지만 적재적소에 사용하면 프로그래머가 얻을 수 있는 이익은 상당하다

# 계산기를 떠올려보자 계산기에 숫자 3을 입력하고 + 기호를 입력한 후 4를 입력하면 결과값으로 7을 보여준다
# 다시 한번 + 기호를 입력한 후 3을 입력하면 기존 결과값 7에 3을 더한 10을 보여준다
# 즉 계산기는 이전에 계산한 결과값을 항상 메모리 어딘가에 저장하고 있어야 한다

# 이를 우리가 앞에서 익힌 함수를 이용해 구현해보자 계산기의 더하기 기능을 구현한 파이썬 코드는 다음과 같다
result = 0
def add(num):
    global result
    result += num
    return result

print(add(3))
# 3
print(add(4))
# 7
# add 함수는 매개변수 num에 받은 값을 이전에 계산한 결과값에 더한 후 돌려주는 함수이다
# 이전에 계산한 결과값을 유지하기 위해서 result 전역변수(global)를 사용했다
#
# 그런데 만일 한 프로그램에서 2대의 계산기가 필요한 상황이 발생하면 어떻게 해야할까?
# 각 계산기는 각각의 결과값을 유지해야 하기 때문에 위와 같이 add 함수 하나만으로는 결과값을 따로 유지할 수 없다
# 이런 상황을 해결하려면 다음과 같이 함수를 각각 따로 만들어야한다
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
# 3
print(add1(4))
# 7
print(add2(3))
# 3
print(add2(7))
# 10
# 똑같은 일을 하는 add1과 add2 함수를 만들었고 각 함수에서 계산한 결과값을 유지하고 저장하기위한
# 전역변수 result1, result2 가 필요하게 되었다
# 계산기1의 결과값이 계산기2에 아무런 영향을 끼치지 않음을 확인할 수 있다
# 하지만 계산기가 3개, 5개, 10개로 점점 더 많이 필요해진다면 어떻게 해야 할까?
# 그때마다 전역변수와 함수를 추가할 것인가? 여기에 빼기나 곱하기 등의 기능을 추가해야한다면?
#
# 위와 같은 경우에 클래스를 사용하면 다음과 같이 간단하게 해결할 수 있다
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
# 3
print(cal1.add(4))
# 7
print(cal2.add(3))
# 3
print(cal2.add(7))
# 10
# 함수 2개를 사용한 것과 동일한 결과가 출력된다
# Calculator 클래스로 만든 별개의 계산기 cal1, cal2가 각각의 역할을 수행한다 (파이썬에서는 이것을 객체라고 부른다)
# 그리고 계산기 cal1, cal2의 결과값 역시 다른 계산기의 결과값과 상관없이 독립적인 값을 유지한다
# 클래스를 사용하면 계산기 개수가 늘어나더라도 객체를 생성하기만 하면 되기 때문에
# 함수를 사용하는 경우와 달리 매우 간단해진다
# 만약 빼기 기능을 추가하려면 Calculator 클래스에 다음과 같은 빼기 기능 함수를 추가하기만 하면 된다
def sub(self, num):
    self.result -= num
    return self.result

