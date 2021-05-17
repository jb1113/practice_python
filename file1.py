# 파일 읽고 쓰기

# 파일 생성하기
file = open("test.txt", 'w')
file.close()
# 파일을 생성하기 위해 파이썬 내장함수 open을 사용했다
# open 함수는 다음과 같이 "파일이름"과 "파일열기모드"를 입력값으로 받고 결과값으로 파일 객체를 돌려준다
파일객체 = open(파일이름, 파일열기모드)
# 파일 열기 모드의 종류
r   | 읽기모드 - 파일을 읽기만 할 때 사용
w   | 쓰기모드 - 파일에 내용을 쓸 때 사용
a   | 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용
# 파일을 쓰기모드로 열면 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라지고
# 해당 파일이 존재하지 않으면 새로운 파일이 생성된다
# 만약 새 파일을 임의의 위치에 생성하고 싶다면 다음과 같이 작성해야 한다
file = open("/Users/a201903165/Python/Practice/test.txt", 'w')
file.close()
# 위 예에서 file.close()는 열려있는 파일객체를 닫아주는 역할을 한다 사실 이문장은 생략해도 된다
# 프로그램을 종료할 때 파이썬 프로그램이 열려있는 파일의 객체를 자동으로 닫아주기 때문이다
# 하지만 close()를 사용해서 열려있는 파일을 직접 닫아주는 것이 좋다
# 쓰기모드로 열었던 파일을 닫지 않고 다시 사용하려고 하면 오류가 발생하기 때문이다

# 파일을 쓰기모드로 열어 출력값 적기
file = open("test.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다\n" % i
    file.write(data)

file.close()
# 위 프로그램을 다음 프로그램과 비교해보자
for i in range(1, 11):
    data = "%d번째 줄입니다\n" % i
    print(data)
# 두 프로그램의 다른점은 data를 출력하는 방법입니다
# 두번째 방법은 지금껏 사용해왔던 모니터 화면에 출력하는 방법이고
# 첫번째 방법은 모니터 화면 대신 파일에 결과값을 적는 방법이다
# 두 방법의 차이점은 print대신 파일객체의 write함수를 사용한 것 말고는 없다

# 프로그램 외부에 저장된 파일을 읽는 여러가지 방법
# 1. readline() 함수 사용하기
file = open("read.txt", 'r')
line = file.readline()
print(line)
file.close()
# 1번째 줄입니다
# 만약 모든 줄을 읽어서 출력하고 싶다면 다음과 같이 작성한다
file = open("read.txt", 'r')
while True:
    line = file.readline()
    if not line:
        break
    print(line)
file.close()
# 즉 while True: 무한루프 안에서 file.readline()을 사용하여 파일을 계속해서 한줄씩 읽어들인다
# 만약 더 이상 읽을 줄이 없으면 break를 수행한다(readline()은 더이상 읽을 줄이 없을 경우 None을 출력한다)

# 위 프로그램을 다음 프로그램과 비교해보자
while 1:
    data = input()
    if not data:
        break
    print(data)
# 위 예는 사용자의 입력을 받아서 그 내용을 출력하는 경우이다 파일을 읽어서 출력하는 예제와 비교해보자
# 입력을 받는 방식만 다르다는 것을 알 수 있다 file.readline() | input()
# 첫번째는 파일을 사용한 입력방법이고 두번째는 키보드를 사용한 입력방법이다

# 2. readlines() 함수 사용하기
file = open("read.txt", 'r')
lines = file.readlines()
for line in lines:
    print(line)
file.close()
# readlines() 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다
# 따라서 lines는 리스트 ['line1\n', 'line2\n', 'line3\n', ..., 'line10\n'] 이다

# 3. read() 함수 사용하
file = open("read.txt", 'r')
data = file.read()
print(data)
f.close()
# read() 함수는 파일의 내용 전체를 문자열로 돌려준다
# 따라서 위 예의 data는 파일 전체 내용의 문자열이다

# 파일에 새로운 내용 추가하기
# 쓰기모드('w')로 파일을 열 때 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라지게 된다
# 하지만 원래 있던 값을 유지하면서 새로운 값을 추가해야 하는 경우에 추가모드('a')를 사용한다
file = open("append.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다\n" % i
    file.write(data)
file.close()
# 추가모드('a')로 파일을 열었기 때문에 기존내용은 남아있고 기존내용 바로 다음부터 결과값을 추가한다

# with문과 함께 사용하기
# 지금까지 살펴본 예제를 보면 항상 다음과 같은 방식으로 파일을 열고 닫았다
file = open("foo.txt", 'w')
file.write("Life is too short, You need python")
file.close()
# 파일을 열면 위와 같이 항상 close 해주는것이 좋다
# 하지만 이렇게 파일을 열고 닫는 것을 자동으로 처리할 수 있다면 편리하지 않을까?
# 파이썬의 with문이 바로 이런 역할을 해준다
# 다음 예는 with문을 사용해서 위 예제를 다시 작성한 모습이다
with open("foo.txt", 'w') as file:
    file.write("Life is too short, You need python")
# 위와 같이 with문을 사용하면 with 블록을 벗어나는 순간 열린 파일객체 file가 자동으로 close된다

# sys 모듈로 매개변수 주기
프롬프트 명령어 [인수1, 인수2, ...]
# 파이썬에는 sys 모듈을 사용하여 매개변수를 직접 줄 수 있다
# sys 모듈을 사용하려면 import 명령어를 사용해야 한다
import sys

args = sys.argv[1:]
for i in args:
    print(i)
# 위 예는 입력받은 인수를 for문을 통해 차례대로 하나씩 출력하는 예이다
# sys 모듈의 argv는 명령 창에서 입력한 인수를 의미한다
# 즉 sys_module.py A B C 과 같이 입력했다면
# argv[0]은 파일이름 sys_module.py 가 되고
# argv[1]부터는 뒤에 따라오는 인수가 차례로 argv의 요소가 된다
# sys_module.py     A       B       C
#   argv[0]     argv[1] argv[2] argv[3]
import sys

args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
# 명령 행에 입력된 소문자를 대문자로 바꾸어주는 프로그램이다
# sys_module.py life is too short, you need python
# LIFE IS TOO SHORT, YOU NEED PYTHON

