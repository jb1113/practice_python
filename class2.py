# 클래스와 객체
# 과자 틀 -> 클래스(class)
# 과자 틀에 의해서 만들어진 과자 -> 객체(object)
# 여기에서 설명할 클래스는 과자 틀과 비슷하다
# 클래스란 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면이고
# 객체란 클래스로 만든 피조물을 뜻한다

# 클래스로 만든 객체에는 중요한 특징이 있다 바로 객체마다 고유한 성격을 가진다는 것이다
# 과자 틀로 만든 과자에 구멍을 뚫거나 조금 베어 먹더라도 다른 과자에는 아무 영향이 없는 것과 마찬가지로
# 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않는다
class Cookie:
    pass
# 다음은 파이썬 클래스의 가장 간단한 예이다
# 위의 클래스는 아무 기능도 갖고 있지 않은 껍질뿐인 클래스다
# 하지만 이렇게 껍질뿐인 클래스도 객체를 생성하는 기능이 있다

# 객체는 클래스로 만들며 1개의 클래스는 무수히 많은 객체를 만들어 낼 수 있다
# 위에서 만든 Cookie 클래스의 객체를 만드는 방법은 다음과 같다
cookie1 = Cookie()
cookie2 = Cookie()
# Cookie()의 결과값을 돌려받은 cookie1, cookie2가 바로 객체이다
# 마치 함수를 사용해서 그 결과값을 돌려받는 모습과 비슷하다

# 객체와 인스턴스의 차이
# 클래스로 만든 객체를 인스턴스라고도 한다 그렇다면 객체와 인스턴스의 차이는 무엇일까?
# cookie1 = Cookie() 이렇게 만든 cookie1은 객체이다 그리고 cookie1 객체는 Cookie의 인스턴스이다
# 즉 인스턴스라는 말은 특정 객체(cookie1)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다



# 사칙연산 클래스 만들기
# 클래스는 무작정 만드는 것보다 클래스로 만든 객체를 중심으로 어떤 식으로 동작하게 할 것인지
# 미리 구상을 한 후에 생각한 것들을 하나씩 해결해가면서 완성해 나가는것이 좋다


# 1. 클래스 구조 만들기
# 가장 먼저 cal = FourCal() 처럼 객체를 만들 수 있게 하기 위해 다음과 같이 만든다
class FourCal:
    pass
# 일단은 아무 기능이 없어도 되기 때문에 매우 간단하게 만들 수 있다
# pass 는 아무것도 수행하지 않는 문법으로 임시로 코드를 작성할 떄 주로 사용한다
cal = FourCal()
type(cal)
# <class '__main__.FourCal'>
# 객체 cal이 FourCal 클래스의 객체임을 알 수 있다
# (type 함수는 파이썬이 자체로 가지고 있는 내장 함수로 객체 타입을 출력한다)


# 2. 객체에 숫자 지정할 수 있게 만들기
# 하지만 생성된 객체 cal은 아직 아무런 기능도 하지 못한다
# 이제 더하기, 빼기, 곱하기, 나누기 등의 기능을 하는 객체를 만들어야 한다
# 그런데 이러한 기능을 갖춘 객체를 만들려면 우선 cal 객체에 사칙연산을 할 때 필요한
# 2개의 숫자를 먼저 알려주어야 한다
# 다음과 같이 연산을 수행할 대상을 객체에 지정할 수 있게 만들어보자
# cal.setData(4, 2)
class FourCal:
    def setData(self, first, second):
        self.first = first
        self.second = second
# 앞에서 만든 FourCal 클래스의 pass 문장을 삭제하고 그 대신 setData 함수를 만들었다
# 클래스 내부에 구현된 함수는 다른 말로 메서드(Method)라고 부른다
# 일반적으로 함수를 만들 떄 다음과 같이 작성한다
def 함수명(매개변수):
    수행할 문장
    ...
# 메서드도 클래스에 포함되어 있다는 점만 제외하면 일반 함수와 다를것이 없다
# setData 메서드를 다시 보면 다음과 같다
def setData(self, first, second):   # 1. 메서드의 매개변수
    self.first = first              # 2. 메서드의 수행문
    self.second = second            # 2. 메서드의 수행문

# 1) setData 메서드의 매개변수
# setData 메서드는 매개변수로 self, first, second 3개 입력값을 받는다
# 그런데 일반 함수와는 달리 메서드의 첫 번째 매개변수 'self' 는 특별한 의미를 가진다
# 다음과 같이 객체 cal을 만들고 cal 객체를 통해 setdata 메서드를 호출해보자
cal = FourCal()
cal.setData(4, 2)
# 객체를 통해 클래스의 메서드를 호출하려면 위와 같이 도트(.) 연산자를 사용해야 한다
# setData 메서드에는 self, first, second 총 3개의 매개변수가 필요한데
# 실제로는 cal.setData(4, 2)처럼 2개의 값만 전달했다 왜일까?
# 그 이유는 cal.setData(4, 2)처럼 호출하면 setData 메서드의 첫 번째 매개변수 self에는 setData 메서드를 호출한 객체 cal이 자동으로 전달되기 때문이다

# self 매개변수는 메서드를 호출한 객체가 전달된다
# 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다
# 객체를 호출할 때 호출한 객체 자신이 전달되기 때문에 self를 사용한 것이다
# 물론 self말고 다른 이름을 사용해도 상관없다
# 메서드의 첫 번째 매개변수 self를 명시적으로 구현하는 것은 파이썬만의 독특한 특징이다
# (예를 들어 자바 같은 언어는 첫 번째 매개변수 self가 필요없다)

# 메서드의 또 다른 호출 방법
# 잘 사용하지는 않지만 클래스를 통해 메서드를 호출하는 것도 가능하다
cal = FourCal()
FourCal.setData(cal, 4, 2)
# 위와 같이 "클래스이름.메서드" 형태로 호출할 때는 객체 cal을 첫 번째 매개변수 self에 꼭 전달해 주어야 한다
# 반면에 다음처럼 "객체.메서드" 형태로 호출할 대는 self를 반드시 생략해서 호출해야 한다
cal = FourCal()
cal.setData(4, 2)

# 2) setData 메서드의 수행문
# cal.setData(4, 2)처럼 호출하면 setData 메서드의 매개변수 first, second에는 각각 값 4와 2가 전달된다
self.first = 4
self.second = 2
# self는 전달된 객체 cal 이므로 다시 다음과 같이 해석된다
cal.first = 4
cal.second = 2
# cal.first = 4 문장이 수행되면 cal 객체에 객체변수 first가 생성되고 값 4가 저장된다
# 마찬가지로 cal.second = 2 문장이 수행되면 cal 객체에 객체변수 second가 생성되고 값 2가 저장된다
# (객체에 생성되는 객체만의 변수를 객체변수라고 부른다)
# 다음과 같이 확인해보자
cal = FourCal()
cal.setData(4, 2)
print(cal.first)
# 4
print(cal.second)
# 2
# cal 객체에 객체변수 first와 second가 생성되었음을 확인할 수 있다
# 이번에는 다음과 같이 cal1, cal2 객체를 만들어보자
cal1 = FourCal()
cal2 = FourCal()
# 그리고 cal1 객체의 객체변수 first를 다음과 같이 생성한다
cal1.setData(4, 2)
print(cal1.first)
# 4
# 이번에는 cal2 객체의 객체변수 first를 다음과 같이 생성한다
cal2.setData(3, 7)
print(cal2.first)
# 3
# 그럼 여기서 cal2 객체의 객체변수 first에는 값 3이 저장된다는 것을 확인할 수 있다
# 그렇다면 cal1 객체의 first는 3으로 변할까? 아니면 기존 값 4를 유지할까?
print(cal1.first)
# 4
# cal1 객체의 first 값은 cal2 객체의 first 값에 영향을 받지 않고 원래 값을 유지하고 있음을 확인할 수 있다
# 이 예제를 통해 확인할 수 있는 바는 아래와 같다
# 클래스로 만든 객체의 객체변수는 다른객체의 객체변수에 상관없이 독립적인 값을 유지한다
# id 함수를 사용하면 객체변수가 독립적인 값을 유지한다는 점을 좀 더 명확하게 증명할 수 있다
# (id 함수는 객체의 주소를 돌려주는 파이썬 내장 함수다)
cal1 = FourCal()
cal2 = FourCal()
cal1.setData(4, 2)
cal2.setData(3, 7)
id(cal1.first)  # cal1의 first 주소값 확인
# 1839194944
id(cal2.first)  # cal2의 first 주소값 확인
# 1839193928
# cal1 객체의 first 주소값과 cal2 객체의 first 주소값이 서로 다르므로 각각 다른곳에 그 값이 저장된다는것을 알 수있다
# 객체변수는 그 객체의 고유 값을 저장할 수 있는 공간이다
# 객체변수는 다른객체들의 영향받지 않고 독립적으로 그 값을 유지한다는 것을 기억하자


# 3. 더하기 기능 만들기
# 2개의 숫자 값을 설정해 주었으니 2개의 숫자를 더하는 기능을 방금 만든 클래스에 추가해보자
class FourCal:
    def setData(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
# 새롭게 추가된 것은 add 메서드이다 이제 클래스를 사용해보자
cal = FourCal()
cal.setData(4, 2)
# 위와 같이 호출하면 앞에서 살펴보았듯이 cal객체의 first, second 객체변수에는 각각 값 4와 2가 저장된다
# 이제 add 메서드를 호출해보자
print(cal.add())
# 6
# cal.add() 라고 호출하면 add 메서드가 호출되어 값 6이 출력될 것이다
# 어떤 과정을 거쳐 값 6이 출력되는지 add 메서드를 따로 떼어 내서 자세히 살펴보자
def add(self):
    result = self.first + self.second
    return result
# add 메서드의 매개변수는 self이고 반환값은 result이다
# 반환 값인 result를 계산하는 부분은 다음과 같다
result = self.first + self.second
# cal.add()와 같이 cal 객체에 의해 add 메서드가 수행되면
# add 메서드의 self에는 객체 cal이 자동으로 입력되므로 다음과 같이 해석한다
result = cal.first + cal.second
# 위 내용은 cal.add() 메서드 호출 전에 cal.setData(4, 2)가 먼저 호출되어
# cal.first = 4, cal.second = 2라고 이미 설정되었기 때문에 다시 다음과 같이 해석한다
result = 4 + 2
# 따라서 다음과 같이 cal.add()를 호출하면 6을 돌려준다
print(cal.add())
# 6


# 4. 빼기, 곱하기, 나누기 기능 만들기
class FourCal:
    def setData(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

# 제대로 동작하는지 확인해보자
cal1 = FourCal()
cal2 = FourCal()
cal1.setData(4, 2)
cal2.setData(3, 8)

cal1.add()
# 6
cal1.sub()
# 2
cal1.mul()
# 8
cal1.div()
# 2.0

cal2.add()
# 11
cal2.sub()
# -5
cal2.mul()
# 24
cal2.div()
# 0.375

