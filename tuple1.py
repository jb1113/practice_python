# 튜플 자료형

# 튜플은 어떻게 만들까?
# 튜플(tuple)은 몇가지 점을 제외하곤 리스트와 거의 비슷하며 리스트와 다른 점은 다음과 같다
# 1. 리스트는 [ ] 으로 둘러싸지만 튜플은 ( ) 으로 둘러싼다
# 2. 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다

# 튜플의 모습은 다음과 같다
t1 = ()
t2 = (1, )
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
# 리스트와 모습은 거의 비슷하지만 튜플에서는 리스트와 다른 2가지 차이점을 찾아볼 수 있다
# t2 = (1,)처럼 단지 1개의 요소만을 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다는 것과 t4 = 1, 2, 3 처럼 괄호()를 생략해도 무방하다는 점이다
# 얼핏 보면 튜플과 리스트는 비슷한 역할을 하지만 프로그래밍을 할 때 튜플과 리스트는 구별해서 사용하는 것이 유리하다
# 튜플과 리스트의 가장 큰 차이는 값을 변화시킬 수 있는가 여부이다
# 즉 리스트의 항목 값은 변화가 가능하고 튜플의 항목 값은 변화가 불가능하다
# (따라서 프로그램이 실행되는 동안 그 값이 항상 변하지 않기를 바란다거나 값이 바뀔까 걱정하고 싶지 않다면 주저하지 말고 튜플을 사용해야 한다)

# 튜플의 요소값을 지우거나 변경하려고 하면 어떻게 될까?
# 1. 튜플 요소값을 삭제하려 할 때
t1 = (1, 2, 'a', 'b')
del t1[0]
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object doesn't support item deletion

# 2. 튜플 요소값을 변경하려 할 때
t1 = (1, 2, 'a', 'b')
t1[0] = 'c'
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
