# 생성자(Constructor)

# 이번에는 이전에 만든 FourCal 클래스를 다음과 같이 사용해보자
cal = FourCal()
cal.add()
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "<stdin>", line 6, in add
# AttributeError: 'FourCal' object has no attribute 'first'

# FourCal 클래스의 인스턴스 cal에 setData 메서드를 수행하지 않고 add 메서드를 수행하면
# "AttributeError: 'FourCal' object has no attribute 'first'" 오류가 발생한다
# setData 메서드를 수행해야 객체 cal의 객체변수 first와 second가 생성되기 때문이다

# 이렇게 객체에 초기값을 설정해야 할 필요가 있을때는 setData와 같은 메서드를 호출하여 초기값을 설정하기 보다는
# 생성자를 구현하는 것이 안전한 방법이다
# 생성자란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다
# 파이썬 메서드 이름으로 __init__를 사용하면 이 메서드는 생성자가 된다
# (__init__ 메서드의 init 앞뒤로 붙은 __는 언더스코어(_) 두개를 붙여 쓴 것이다)

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setData(self, first, second):
        self.first = first
        self.second = second
    ...
# 새롭게 추가된 생성자 __init__ 메서드만 따로 떼어 내서 살펴보자
def __init__(self, first, second):
    self.first = first
    self.second = second
# __init__ 메서드는 setData 메서드와 이름만 다르고 모든게 동일하다
# 단 메서드 이름을 __init__으로 했기 때문에 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출된다

# 이제 다음과같이 에제를 수행해보자
cal = FourCal()
# Traceback (most recent call last):
#  File "<stdin>", lin1, in <module>
# TypeError: __init__() missing 2 required positional arguments: 'first' and 'second'
# cal = FourCal() 을 수행할 때 생성자 __init__이 호출되어 위와 같은 오류가 발생했다
# 오류가 발생한 이유는 생성자의 매개변수 first와 second에 해당하는 값이 전달되지 않았기 때문이다
# 위 오류를 해결하려면 다음처럼 first와 second에 해당되는 값을 전달하여 객체를 생성해야 한다
cal = FourCal(4, 2)
# 위와 같이 수행하면 __init__ 메서드의 매개변수에 각각 값이 대입된다
self    | 생성되는 객체
first   | 4
second  | 2
# __init__ 메서드도 다른 메서드와 마찬가지로 첫 번째 매개변수 self에 생성되는 객체가 자동으로 전달된다
# 따라서 __init__ 메서드가 호출되면 setData 메서드를 호출했을 떄와 마찬가지로 first와 second라는 객체변수가 생성된다
# 다음과 같이 객체변수의 값을 확인해보자
cal = FourCal(4, 2)
print(cal.first)
# 4
print(cal.second)
# 2
# add나 div 등의 메서드도 잘 동작한다
cal.add()
# 6
cal.div()
# 2.0

