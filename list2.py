# 리스트 연산하기

# 리스트 더하기
a = [1, 2, 3]
b = [4, 5, 6]
a + b
# [1, 2, 3, 4, 5, 6]

# 리스트 반복하기
a = [1, 2, 3]
a * 3
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 리스트 길이 구하기
a = [1, 2, 3]
len(a)
# 3

# 초보자가 범하기 쉬운 리스트 연산 오류
a = [1, 2, 3]
a[2] + "hi"
# 결과 값은?
# a[2]의 값인 3과 문자열 hi가 더해져서 3hi가 출력될 것이라고 생각할 수 있다
# 하지만 형 오류(TypeError)가 발생했다
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# a[2]에 저장된 값은 3이라는 정수인데 "hi"는 문자열이다
# 정수와 문자열을 당연히 서로 더할 수 없기 때문에 형 오류가 발생한 것이다
# 만약 숫자와 문자열을 더해서 "3hi"처럼 만들고 싶다면 숫자 3을 문자 '3'으로 바꾸어 주어야 한다
# str(a[2]) + "hi"
# str() 함수는 정수나 실수를 문자열의 형태로 바꾸어 주는 파이썬의 내장함수이다

