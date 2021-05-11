# 제어문
# if문

# if문의 기본 구조
if 조건문:
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장A
    수행할 문장B
    ...

money = True
if money:
    print("taxi")
else:
    print("walking")
# 'taxi'

# 들여쓰기
if 조건문:
    수행할 문장1
    수행할 문장2
    수행할 문장3
-> Correct

if 조건문:
    수행할 문장1
수행할 문장2
    수행할 문장3
-> Error

if 조건문:
    수행할 문장1
    수행할 문장2
        수행할 문장3
-> Error
# 들여쓰기의 너비가 다르다 들여쓰기는 언제나 같은 너비로 해야 한다
#
# 들여쓰기는 공백으로 하는 것이 좋을까? 아니면 탭으로 하는것이 좋을까?
# 2가지를 혼용해서 쓰면 안된다 공백으로 할 거면 항상 공백으로 통일하고 탭으로 할 거면 항상 탭으로 통일한다
# 요즘 파이썬 커뮤니티에서는 들여쓰기를 할 때 공백 4개를 사용하는 것을 권장한다
#
# 조건문 다음에 콜론(:)을 잊지 말자
# if 조건문 뒤에는 반드시 콜론(:)이 붙는다 어떤 특별한 의미가 있다기보다는 파이썬의 문법 구조이다
# 앞으로 배울 while이나 for, def, class문에도 역시 문장의 끝에 콜론(:)이 항상 들어간다
# 다른 언어에서는 if문을 { } 기호로 감싸지만 파이썬에서는 들여쓰기로 구분한다

# 비교연산자
money = 2000
if money >= 3000:
    print("taxi")
else:
    print("walking")
# 'walking'

# and, or, not
x or y
x and y
not x

money = 2000
card = True
if money >= 3000 or card:
    print("taxi")
else:
    print("walking")
# 'taxi'

# x in s, x not in s
# x in 리스트   | x not in 리스트
# x in 튜플     | x not in 튜플
# x in 문자열   | x not in 문자열
1 in [1, 2, 3]
# True
1 not in [1, 2, 3]
# False
'a' in ('a', 'b', 'c')
# True
'j' not in 'python'
# True

# 만약 주머니에 돈이 있으면 택시를 타고 없으면 걸어 가라
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("taxi")
else:
    print("walking")
# 'taxi'

# 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
# 가끔 조건문의 참, 거짓에 다라 실행할 행동을 정의할 때 아무런 일도 하지 않도록 설정하고 싶을 때가 있다
# 주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라
# 이럴때 사용하는 것이 바로 pass이다
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("take out a card")
# pocket 리스트 안에 money 문자열이 있기 때문에 if문 다음 문장인 pass가 수행되고 아무 결과값도 보여주지 않는다



# 다양한 조건을 판단하는 elif
# if, elif, else 기본 구조
if 조건문:
    수행할 문장1
    수행할 문장2
elif 조건문:
    수행할 문장3
    수행할 문장4
elif 조건문:
    수행할 문장5
    수행할 문장6
...
else:
    수행할 문장A
    수행할 문장B

# 주머니에 돈이 있으면 택시를 타고 주머니에 돈은 없지만 카드가 있으면 택시를 타고 돈도 없고 카드도 없으면 걸어 가라
pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("taxi")
else:
    if card:
        print("taxi")
    else:
        print("walking")
# 'taxi'

# elif 사용 (다중 조건)
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("taxi")
elif card:
    print("taxi")
else:
    print("walking")
# 'taxi'

# if문을 한줄로 작성하기
# if문 다음에 수행할 문장이 한줄일때 조금 더 간략하게 코드를 작성할 수 있다
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("take out a card")
# if문 다음 수행할 문장을 콜론(:) 뒤에 바로 적어 준다



# 조건부 표현식
조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
# 조건부 표현식은 가동성에 유리하고 한 줄로 작성할 수 있어 활용성이 좋다
if score >= 60:
    message = "success"
else:
    message = "failure"

# 조건부 표현식(conditional expression) 사용
message = "success" if score >= 60 else "failure"

