# 딕셔너리 자료형

# 딕셔너리란?
# 사람은 누구든지 "이름" = "홍길동", "생일" = "몇월몇일" 등으로 구별할 수 있다 파이썬은 영리하게도 이러한 대응 관계를 나타낼 수 있는 자료형을 가지고 있다
# 요즘 사용하는 대부분의 언어도 이러한 대응 관계를 나타내는 자료형을 갖고 있는데, 이를 연관 배열(Associative array) 또는 해시(Hash)라고 한다
# 파이썬에서는 이러한 자료형을 딕셔너리(Dictionary)라고 하는데 단어 그대로 해석하면 사전이라는 뜻이다
# 즉, "people"이라는 단어에 "사람", "baseball"이라는 단어에 "야구"라는 뜻이 부합되듯이 딕셔너리는 Key와 Value를 한 쌍으로 갖는 자료형이다
# 예컨대 Key가 "baseball"이라면 Value는 "야구"가 될 것이다

# 딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요소값을 구하지 않고 Key를 통해 Value를 얻는다
# 이것이 바로 딕셔너리의 가장 큰 특징이다
# baseball이라는 단어의 뜻을 찾기 위해 사전의 내용을 순차적으로 모두 검색하는 것이 아니라 baseball이라는 단어가 있는 곳만 펼쳐 보는 것이다

# 딕셔너리는 어떻게 만들까?
# 다음은 기본 딕셔너리의 모습이다
# {Key1:Value1, Key2:Value2, Key3:Value3, ...}
# Key와 Value의 쌍 여러 개가 { } 로 둘러싸여 있다 각각의 요소는 Key : Value 형태로 이루어져 있고 쉼표(,)로 구분되어 있다
# * Key에는 변하지 않는 값을 사용하고 Value에는 변하는 값과 변하지 않는 값 모두 사용할 수 있다 *

# 다음 딕셔너리 예를 살펴보자
dictionary = {'name':'JB', 'phone':'01012345678', 'birth':'1113'}
# 위에서 Key는 각각 'name', 'phone', 'birth'이고 각각의 Key에 해당하는 Value는 'JB', '01012345678', '1113'이 된다

# 다음 예는 Key로 정수 값 1, Value로 문자열 'hello'를 사용한 예이다
a = {1 : 'hello'}
# 또한 다음 예처럼 Value에 리스트도 넣을 수 있다
a = {'a' : [1, 2, 3]}

# 딕셔너리 쌍 추가, 삭제하기
a = {1 : 'a'}
a[2] = 'b'
a
# {1 : 'a', 2 : 'b'}
# {1 : 'a'} 딕셔너리에 a[2] = 'b'와 같이 입력하면 딕셔너리 a에 Key와 Value가 각각 2와 'b'인 2 : 'b' 라는 딕셔너리 쌍이 추가된다
a['name'] = 'JB'
a
# {1 : 'a', 2 : 'b', 'name' : 'JB'}
a[3] = [1, 2, 3]
a
# {1 : 'a', 2 : 'b', 'name' : 'JB', 3 : [1, 2, 3]}

# 딕셔너리 요소 삭제하기
del a[1]
a
# {2 : 'b', 'name' : 'JB', 3 : [1, 2, 3]}
# 위 예제는 딕셔너리 요소를 지우는 방법을 보여준다 del 함수를 사용해서 del a[Key]처럼 입력하면 지정한 Key에 해당하는 {key : value} 쌍이 삭제된다

# 딕셔너리를 사용하는 방법
# 딕셔너리에서 Key 사용해 Value 얻기
grade = {'julliet' : 100, 'romeo' : 90}
grade['romeo']
# 90
grade['julliet']
# 100
# 리스트나 튜플, 문자열은 요소값을 얻고자 할 떄 인덱싱이나 슬라이싱 기법 중 하나를 사용했다
# 하지만 딕셔너리는 단 한가지 방법 뿐이다
# 바로 Key를 사용해서 Value를 구하는 방법이다
# 어떤 Key의 Value를 얻기 위해서는 딕셔너리변수이름[Key]를 사용한다
a = {1 : 'a', 2 : 'b'}
a[1]
# 'a'
a[2]
# 'b'
# 먼저 a 변수에 {1 : 'a', 2 : 'b'} 딕셔너리를 대입했다 위 예에서 볼 수 있듯이 a[1]은 'a'값을 돌려준다
# 여기에서 a[1]이 의미하는 것은 리스트나 튜플의 a[1]과는 전혀 다르다
# 딕셔너리 변수에서 [ ] 안의 숫자 1은 두 번째 요소를 뜻하는 것이 아니라 Key에 해당하는 1을 나타낸다
# 딕셔너리는 리스트나 튜플에 있는 인덱싱 방법을 적용할 수 없다
a = {'a' : 1, 'b' : 2}
a['a']
# 1
a['b']
# 2
dic = {'name' : 'JB', 'phone' : '01012345678', 'birth' : '1113'}
dic['name']
# 'JB'
dic['phone']
# '01012345678'
dic['birth']
# '1113'



# 딕셔너리 만들 때 주의사항
# 먼저 딕셔너리에서 Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다는 점을 주의해야 한다
# 다음 예에서 볼 수 있듯이 동일한 Key가 2개 존재할 경우 1 : 'a' 쌍이 무시된다
a = {1 : 'a', 1 : 'b'}
a
# {1 : 'b'}
# 이렇게 Key가 중복되었을 때 1개를 제외한 나머지 Key:Value 값이 모두 무시되는 이유는 Key를 통해서 Value를 얻는 딕셔너리의 특징에서 비롯된다
# 즉 동일한 Key가 존재하면 어떤 Key에 해당하는 Value를 불러야 할지 알 수 없기 때문이다
# 또 한 가지 주의해야 할 사항은 Key에 리스트는 쓸 수 없다는 것이다
# 하지만 튜플은 Key로 쓸 수 있다
# 딕셔너리의 Key로 쓸 수 있느냐 없느냐는 Key가 변하는 값인지 변하지 않는 값인지에 달려 있다
# 리스트는 그 값이 변할 수 있기 때문에 Key로 쓸 수 없다
a = {[1, 2] : 'hello'}
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'
# 따라서 딕셔너리의 Key 값으로 딕셔너리를 사용할 수 없음은 당연하다
# 단 Value에는 변하는 값이든 변하지 않는 값이든 상관없이 아무 값이나 넣을 수 있다

