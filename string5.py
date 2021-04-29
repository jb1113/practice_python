# 문자열 관련 함수들
# 문자열 자료형은 자체적으로 함수를 가지고 있다 이들 함수를 다른 말로 문자열 내장 함수라 한다
# 이 내장 함수를 사용하려면 문자열 변수 이름 뒤에 '.'를 붙인 다음에 함수 이름을 써주면 된다

# 문자 개수 세기 (count)
word = "hello"
word.count('l')
# 2

# 위치 알려주기1 (find)
str = "Python is the best choice"
str.find('b')
# 14
str.find('k')
# -1
# 문자열 중 'b'가 처음 나온 위치를 반환한다
# 만약 찾는 문자나 문자열이 존재하지 않는다면 '-1'을 반환한다

# 위치 알려주기2 (index)
str = "Life is too short"
str.index('t')
# 8
str.index('k')
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ValueError: substring not found
# 문자열 중 't'가 처음 나온 위치를 반환한다
# 만약 찾는 문자나 문자열이 존재하지 않는다면 오류를 발생시킨다

# 문자열 삽입 (join)
",".join('abcd')
# 'a,b,c,d'
# abcd 문자열의 각각의 문자 사이에 ','를 삽입한다
# join 함수는 문자열뿐만 아니라 앞으로 배울 리스트나 튜플도 입력으로 사용할 수 있다
",".join(['a', 'b', 'c', 'd'])
# 'a,b,c,d'

# 소문자를 대문자로 바꾸기 (upper)
str = "hello"
str.upper()
# 'HELLO'

# 대문자를 소문자로 바꾸기 (lower)
str = "HELLO"
str.lower()
# 'hello'

# 왼쪽 공백 지우기 (lstrip)
str = " hello "
str.lstrip()
# 'hello '

# 오른쪽 공백 지우기 (rstrip)
str = " hello "
str.rstrip()
# ' hello'

# 양쪽 공백 지우기 (strip)
str = " hello "
str.strip()
# 'hello'

# 문자열 바꾸기 (replace)
str = "Life is too short"
str.replace("Life", "Your leg")
# 'Your leg is too short'

# 문자열 나누기 (split)
str1 = "Life is too short"
str1.split()
# ['Life', 'is', 'too', 'short']
str2 = "A:B:C:D"
str2.split(':')
# ['A', 'B', 'C', 'D']
# split 함수는 str.split()처럼 괄호 안에 아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다
# 만약 str.split(':')처럼 괄호 안에 특정 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나누어 준다
# 이렇게 나눈 값은 리스트에 하나씩 들어가게 된다

