# 예외 처리

# 오류는 어떤 때 발생하는가?
# 디렉터리 안에 없는 파일을 열려고 시도하는 경우
file = open("없는파일", 'r')
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# FileNotFoundError: [Errorno 2] No such file or directory: '없는파일'
# 위 예에서 볼 수 있듯이 없는 파일을 열려고 시도하면 FileNotFoundError 오류가 발생한다

# 0으로 다른 숫자를 나누는 경우
4 / 0
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# 4를 0으로 나누려니까 ZeroDivisionError 오류가 발생한다

# 잘못된 index에 접근하는 경우
A = [1, 2, 3]
A[4]
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# A는 리스트 [1, 2, 3]인데 A[4]는 A 리스트에서 얻을 수 없는 값이다 따라서 IndexError 오류가 발생한다
# 파이썬은 이런 오류가 발생하면 프로그램을 중단하고 오류 메세지를 보여준다

# 오류 예외 처리 기법
# try, except문
# 오류처리를 위한 try, except 문의 기본 구조
try:
    ...
except [발생오류[as 오류메세지 변수]]:
    ...
# try 블록 수행 중 오류가 발생하면 except 블록이 수행된다 하지만 try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다
# except 구문을 자세히 살펴보자
except [발생오류[as 오류메세지 변수]]:
# 위 구문을 보면 [] 기호를 사용하는데 이 기호는 괄호 안의 내용을 생략할 수 있다는 관례 표기법이다
# 즉 except 구문은 다음 3가지 방법으로 사용할 수 있다
# 1. try, except만 쓰는 방법
try:
    ...
except:
    ...
# 이 경우는 오류 종류에 상관없이 오류가 발생하면 except 블록을 수행한다
#
# 2. 발생 오류만 포함한 except문
try:
    ...
except 발생오류:
    ...
# 이 경우는 오류가 발생했을때 except문에 미리 정해놓은 오류 이름과 일치할 때만 except 블록을 수행한다는 뜻이다
#
# 3. 발생 오류와 오류메세지 변수까지 포함한 except문
try:
    ...
except 발생오류 as 오류메세지 변수:
    ...
# 이 경우는 두번째 경우에서 오류 메세지의 내용까지 알고 싶을때 사용하는 방법이다
# 이 방법의 예를 들어보면 다음과 같다
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
# division by zero
# 위처럼 4를 0으로 나누려고 하면 ZeroDivisionError가 발생하여 except 블록이 실행되고 변수 e에 담기는 오류메세지를 위와 같이 출력한다

# try.. finally
# try문에는 finally절을 사용할 수 있다
# finally 절은 try문 수행 도중 예외발생 여부에 상관없이 항상 수행된다
# 보통 finally절은 사용한 리소스를 close해야 할때에 많이 사용한다
file = open("foo.txt", 'w')
try:
    # 무언가를 수행한다
finally:
    file.close()
# foo.txt 파일을 쓰기 모드로 연 후에 try문을 수행한 후 예외 발생 여부와 상관없이 finally절에서 file.close()로 열린파일을 닫을수 있다

# 여러개의 오류 처리하기
# try문 안에서 여러개의 오류를 처리하기 위해 다음 구문을 사용한다
try:
    ...
except 발생오류1:
    ...
except 발생오류2:
    ...
# 즉 0으로 나누는 오류와 인덱싱 오류를 다음과 같이 처리할 수 있다
try:
    A = [1, 2]
    print(A[3])
    4 / 0
except ZeroDivisionError:
    print("0으로 나눌수 없습니다")
except IndexError:
    print("인덱싱 할 수 없습니다")
# A는 2개의 요소값을 가지고 있기때문에 A[3]은 IndexError를 발생시키므로 "인덱싱 할 수 없습니다"라는 문자열이 출력될 것이다
# 인덱싱 오류가 먼저 발생했으므로 4 / 0으로 발생되는 ZeroDivisionError 오류는 발생하지 않았다
# 앞에서 알아본 것과 마찬가지로 오류메세지도 다음과 같이 가져올 수 있다
try:
    A = [1, 2]
    print(A[3])
    4 / 0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
# 프로그램을 실행하면 "list index out of range" 오류메세지가 출력될 것이다
# 다음과 같이 ZeroDivisionError와 IndexError를 함께 처리할 수도 있다
try:
    A = [1, 2]
    print(A[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)
# 2개 이상의 오류를 동시에 처리하기 위해서는 위와 같이 괄호를 사용하여 함께 묶어 처리하면 된다

