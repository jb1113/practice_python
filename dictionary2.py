# 딕셔너리 관련 함수들

# Key 리스트 만들기 (keys)
a = {'name' : 'JB', 'phone' : '01012345678', 'birth' : '1113'}
a.keys()
# dict_keys(['name', 'phone', 'birth'])
# keys()는 딕셔너리의 Key만을 모아서 dict_keys 객체를 돌려준다

# 파이썬 3.0 이후 버전의 keys 함수 어떻게 달라졌나?
# 파이썬 2.7 버전까지는 keys() 함수를 호출할 때 반환 값으로 dict_keys가 아닌 리스트를 돌려준다
# 리스트를 돌려주기 위해서는 메모리 낭비가 발생하는데 파이썬 3.0 이후 버전에서는 이러한 메모리 낭비를 줄이기 위해 dict_keys 객체를 돌려준다
# 다음에 소개할 dict_values, dict_items 역시 파이썬 3.0 이후 버전에서 추가된 것들이다
# 만약 3.0 이후 버전에서 반환 값으로 리스트가 필요한 경우에는 list(a.keys())를 사용하면 된다
# dict_keys, dict_values, dict_items 등은 리스트로 변환하지 않더라도 기본적인 반복(iterate) 구문을 실행할 수 있다

# dict_keys 객체는 다음과 같이 사용할 수 있다 리스트를 사용하는 것과 차이가 없지만 리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없다
for k in a.keys():
    print(k)
# name
# phone
# birth
#
# dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면 된다
list(a.keys())
# ['name', 'phone', 'birth']

# Value 리스트 만들기 (values)
a.values()
# dict_values(['JB', '01012345678', '1113'])
# Key를 얻는 것과 마찬가지 방법으로 Value만 얻고 싶다면 values 함수를 사용하면 된다 values 함수를 호출하면 dict_values 객체를 돌려준다

# Key, Value 쌍 얻기 (items)
a.items()
# dict_items([('name', 'JB'), ('phone', '01012345678'), ('birth', '1113')])
# items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다
# dict_values 객체와 dict_items 객체 역시 dict_keys 객체와 마찬가지로 리스트를 사용하는 것과 동일하게 사용할 수 있다

# Key:Value 쌍 모두 지우기 (clear)
a.clear()
a
# {}
# clear 함수는 딕셔너리 안의 모든 요소를 삭제한다
# 빈 리스트를 [], 빈 튜플을 ()로 표현하는 것과 마찬가지로 빈 딕셔너리도 {}로 표현한다

# Key로 Value얻기 (get)
a.get('name')
# 'JB'
a.get('birth')
# '1113'
# get(x) 함수는 x라는 Key에 대응되는 Value를 돌려준다
# 앞에서 살펴보았듯이 a.get('name')은 a['name']을 사용했을 때와 동일한 결과값을 돌려받는다
# 다만 다음 예제에서 볼 수 있듯이 a['noKey']처럼 존재하지 않는 키(noKey)로 값을 가져오려고 할 경우
# a['noKey']는 Key 오류를 발생시키고 a.get('noKey')는 None을 돌려준다는 차이가 있다
# ( None은 "거짓"이라는 뜻이다 )
print(a.get('noKey'))
# None
print(a['noKey'])
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# KeyError: 'noKey'
#
# 딕셔너리 안에 찾으려는 Key 값이 없을 경우 미리 정해둔 디폴트 값을 대신 가져오게 하고 싶을 떄에는 get(x, '디폴트값')을 사용한다
a.get('foo', 'bar')
# 'bar'

# 해당 Key가 딕셔너리 안에 있는지 조사하기 (in)
'name' in a
# True
'email' in a
# False

