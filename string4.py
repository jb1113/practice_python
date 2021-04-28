# 문자열 포매팅
# 문자열 안에 어떤 값을 삽입하는 방법

# 숫자 바로 대입
"I eat %d apples." % 3
# 'I eat 3 apples.'

# 문자열 바로 대입
"I eat %s apples." % "five"
# 'I eat five apples.'

# 숫자 값을 나타내는 변수로 대입
number = 3
"I eat %d apples." % number
# 'I eat 3 apples.'

# 2개 이상의 값 넣기 (% 다음 괄호 안에 콤마(,)로 구분)
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)
# 'I ate 10 apples. so I was sick for three days.'

# %s 포맷코드는 어떠한 형태의 값이든 변환해 넣을 수 있다
"I have %s apples" % 3
# 'I have 3 apples'
"rate is %s" % 3.234
# 'rate is 3.234'
# %s는 자동으로 % 뒤에 있는 값을 문자열로 바꾼다

# 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
"Error is %d%." % 98
-> Error
# 문자열 포맷 코드인 %d와 %가 같은 문자열 안에 존재하는 경우, %를 나타내려면 반드시 %%로 써야 한다
# 하지만 문자열 안에 %d같은 포매팅 연산자가 없으면 %는 홀로 쓰여도 상관 없다
"Error is %d%%." % 98
-> Correct

# 포맷 코드와 숫자 함께 사용하기
# 1. 정렬과 공백
"%10s" % "hi"
# '        hi'
"%-10sjane." % "hi"
# 'hi          jane.'

# 2. 소수점 표현
"%0.4f" % 3.42134234
# '3.4213'
"%10.4f" % 3.42134234
# '    3.4213'



# format 함수를 사용한 포매팅
# 숫자 바로 대입
"I eat {0} apples".format(3)
# 'I eat 3 apples'

# 문자열 바로 대입
"I eat {0} apples".format("five")
# 'I eat five apples'

# 숫자 값을 가진 변수로 대입
number = 3
"I eat {0} apples".format(number)
# 'I eat 3 apples'

# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)
# 'I ate 10 apples. so I was sick for three days.'
# 2개 이상의 값을 넣을 경우 문자열의 {0}, {1}과 같은 인덱스 항목이 format 함수의 입력값으로 순서에 맞게 바뀐다

# 이름으로 넣기
"I ate {number} apples. so I was sick for {day} days.".format(number=10, day="three")
# 'I ate 10 apples. so I was sick for three days.'

# 인덱스와 이름을 혼용해서 넣기
"I ate {0} apples. so I was sick for {day} days.".format(10, day="three")
# 'I ate 10 apples. so I was sick for 3 days.'

# 왼쪽 정렬
"{0:<10}".format("hi")
# 'hi        '
# :<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있다

# 오른쪽 정렬
"{0:>10}".format("hi")
# '        hi'
# 오른쪽 정렬은 :< 대신 :>을 사용하면 된다 (화살표 방향을 생각하면 어느쪽으로 정렬되는지 바로 알 수 있음)

# 가운데 정렬
"{0:^10}".format("hi")
# '    hi    '
# :^ 기호를 사용하여 가운데 정렬 한다

# 공백 채우기
"{0:=^10}".format("hi")
# '====hi===='
"{0:!<10}".format("hi")
# 'hi!!!!!!!!'
# 정렬할 때 공백 문자 대신 지정한 문자 값으로 채워 넣는 것도 가능
# 채워 넣을 문자 값은 정렬 문자 <, >, ^ 바로 앞에 넣어야 함

# 소수점 표현
y = 3.42134234
"{0:0.4f}".format(y)
# '3.4213'
"{0:10.4f}".format(y)
# '    3.4213'

# { 또는 } 문자 표현
"{{ and }}".format()
# '{ and }'



# f 문자열 포매팅 (파이썬 3.6 버전부터 가능)
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
# '나의 이름은 홍길동입니다. 나이는 30입니다.'
# f 문자열 포매팅은 위와 같이 name, age와 같은 변수 값을 생성한 후에 그 값을 참조할 수 있음

# 또한 f 문자열 포매팅은 표현식을 지원하기 때문에 다음과 같은 것도 가능
# (표현식이란 문자열 안에서 변수와 +,-와 같은 수식을 함께 사용하는 것을 말함)
age = 30
f'나는 내년이면 {age+1}살이 된다'
# '나는 내년이면 31살이 된다.'

# 딕셔너리는 f 문자열 포매팅에서 다음과 같이 사용할 수 있음
# (딕셔너리는 Key와 Value라는 것을 한 쌍으로 갖는 자료형이다)
data = {'name':'홍길동', 'age':30}
f'나의 이름은 {data["name"]}입니다. 나이는 {data["age"]}입니다.'
# '나의 이름은 홍길동입니다. 나이는 30입니다.'

# 왼쪽 정렬
f'{"hi":<10}'
# 'hi        '

# 오른쪽 정렬
f'{"hi":>10}'
# '        hi'

# 가운데 정렬
f'{"hi":^10}'
# '    hi    '

# 공백 채우기
f'{"hi":=^10}'
# '====hi===='
f'{"hi":!<10}'
# 'hi!!!!!!!!'

# 소수점 표현
y = 3.42134234
f'{y:0.4f}'
# '3.4213'
f'{y:10.4f}'
# '    3.4213'

# f 문자열에서 { } 문자를 표시하려면 다음과 같이 두 개를 동시에 사용해야 함
f'{{ and }}'
# '{ and }'

