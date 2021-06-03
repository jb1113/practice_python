# 클래스 변수

# 객체변수는 다른 객체들에 영향받지 않고 독립적으로 그 값을 유지한다는 것을 이미 알아보았다
# 이번에는 객체변수와는 성격이 다른 클래스 변수에 대해 알아보자

# 다음 클래스를 작성해보자
class Family:
    lastname = "Smith"
# Family 클래스에 선언한 lastname이 바로 클래스 변수이다
# 클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언하여 생성한다

# 이제 Family 클래스를 다음과 같이 사용해보자
print(Family.lastname)
# 'Smith'
# 클래스 변수는 위 예와 같이 클래스이름.클래스변수로 사용할 수 있다
# 또는 다음과 같이 Family 클래스로 만든 객체를 통해서도 클래스 변수를 사용할 수 있다
familyA = Family()
familyB = Family()
print(familyA.lastname)
# 'Smith'
print(familyB.lastname)
# 'Smith'
# 만약 Family 클래스의 lastname을 다음과 같이 'John'이라는 문자열로 바꾸면 어떻게 될까?
Family.lastname = "John"
print(familyA.lastname)
# 'John'
print(familyB.lastname)
# 'John'
# 클래스 변수 값을 변경했더니 클래스로 만든 다른 객체의 lastname 값도 모두 변경된다는 것을 확인할 수 있다
# 즉 클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징이 있다

# id 함수를 사용하면 클래스 변수가 공유된다는 사실을 증명할 수 있다
id(Family.lastname)
# 4480159136
id(familyA.lastname)
# 4480159136
id(familyB.lastname)
# 4480159136
# id 값이 모두 같으므로 Family.lastname, familyA.lastname, familyB.lastname 은 모두 같은 메모리를 가리키고 있다

