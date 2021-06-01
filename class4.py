# 클래스의 상속
# 상속(Inheritance)이란 어떤 클래스를 만들때 다른 클래스의 기능을 물려받을수 있게 만드는 것이다

# 이번에는 상속을 사용하여 이전에 만든 FourCal 클래스에 a의 b제곱을 구할 수 있는 기능을 추가해보자
# 앞서 FourCal 클래스는 만들었으므로 FourCal 클래스를 상속하는 MoreFourCal 클래스를 만든다
class MoreFourCal(FourCal):
    pass
# 클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어주면 된다
class 클래스이름(상속할 클래스이름)
# MoreFourCal 클래스는 FourCal 클래스를 상속했으므로 FourCal 클래스의 모든 기능을 사용할 수 있어야 한다
# 다음과 같이 확인해보자
cal = MoreFourCal(4, 2)
# 현재로서는 FourCal.py 파일에 FourCal와 MoreFourCal 두 개의 클래스를 정의하였다

# 왜 상속을 해야 할까?
# 보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다
# 클래스에 기능을 추가하고 싶으면 기존 클래스를 수정하면 되는데 왜 굳이 상속을 받아서 처리해야 하지?라는 의문이 들 수도 있다
# 하지만 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야 한다

# 이제 원래 목적인 a의 b제곱을 계산하는 MoreFourCal 클래스를 만들어보자
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
# pass 문장은 삭제하고 위와 같이 두 수의 거듭제곱을 구할 수 있는 pow 메서드를 추가해 주었다
# 다음과 같이 pow 메서드를 수행해보자
cal = MoreFourCal(4, 2)
cal.pow()
# 16
# MoreFourCal 클래스로 만든 cal 객체에 값 4와 2를 설정한 후 pow 메서드를 호출하면 4의 2제곱인 16을 돌려주는 것을 확인할 수 있다
# 상속은 MoreFourCal 클래스처럼 기존 클래스(FourCal)는 그대로 놔둔 채 클래스의 기능을 확장시킬 때 주로 사용한다

