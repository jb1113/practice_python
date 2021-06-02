# 메서드 오버라이딩

# 이번에는 FourCal 클래스를 다음과 같이 실행해보자
cal = FourCal(4, 0)
cal.div()
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#   result = self.first / self.second
# ZeroDivisionError: division by zero
# FourCal 클래스의 객체 cal에 4와 0 값을 설정하고 div 메서드를 호출하면 4를 0으로 나누려고 하기 때문에 위와 같은 ZeroDivisionError 오류가 발생한다
# 하지만 0으로 나눌때 오류가 아닌 0을 돌려주도록 만들고 싶다면 어떻게 해야 할까?

# 다음과 같이 FourCal 클래스를 상속하는 SafeFourCal 클래스를 만들어보자
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
# SafeFourCal 클래스는 FourCal 클래스에 있는 div 메서드를 동일한 이름으로 다시 작성하였다
# 이렇게 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩(Overriding, 덮어쓰기)이라고 한다
# 이렇게 메서드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한 메서드가 호출된다
# SafeFourCal 클래스에 오버라이딩한 div 메서드는 나누는 값이 0인 경우에는 0을 돌려주도록 수정하였다
cal = SafeFourCal(4, 0)
cal.div()
# 0
# FourCal 클래스와는 달리 ZeroDivisionError가 발생하지 않고 의도한 대로 0을 돌려주는 것을 확인할 수 있다

