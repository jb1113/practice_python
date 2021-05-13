# 반복문
# for문

# for문의 기본 구조
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...

# 예제를 통해 for문 이해하기
# 1. 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
# one
# two
# three

# 2. 다양한 for문의 사용
tuple_in_list = [(1, 2), (3, 4), (5, 6)]
for (first, last) in tuple_in_list:
    print(first + last)
# 3
# 7
# 11
# 위 예에서 리스트의 요소값이 튜플이기 때문에 각각의 요소가 자동으로 (first, last) 변수에 대입된다
# 튜플을 사용한 변수값 대입 방법과 비슷한 경우이다
# (first, last) = (1, 2)

# 3. for문의 응용
# 5명의 학생의 시험점수 리스트에서 60점이 넘는 경우 합격, 그렇지 못한 경우 불합격에 해당하는 결과를 출력하라
marks = [90, 24, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다" % number)
    else:
        print("%d번 학생은 불합격입니다" % number)
# 점수 리스트 marks에서 차례로 점수를 꺼내어 mark라는 변수에 대입한다
# 1번 학생은 합격입니다
# 2번 학생은 불합격입니다
# 3번 학생은 합격입니다
# 4번 학생은 불합격입니다
# 5번 학생은 합격입니다

# for문과 continue
# 60점 이상인 사람에게는 축하 메세지를 보내고 나머지 사람에게는 아무 메세지도 전하지 않는다
marks = [90, 24, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다 합격입니다" % number)
# 1번 학생 축하합니다 합격입니다
# 3번 학생 축하합니다 합격입니다
# 5번 학생 축하합니다 합격입니다

# for문과 함께 자주 사용하는 range 함수
# for문은 숫자 리스트를 자동으로 만들어주는 range 함수와 함께 사용하는 경우가 많다
number = range(10)
number
# range(0, 10)
# range(10)은 0부터 10미만의 숫자를 포함하는 range 객체를 만들어 준다

# 시작숫자와 끝숫자를 지정하려면 range(시작숫자, 끝숫자) 형태를 사용하는데 이때 끝숫자는 포함되지 않는다
number = range(1, 11)
number
# range(1, 11)

# range 함수의 예시 살펴보기
# for와 range 함수를 사용하면 1부터 10까지 더하는 것을 다음과 같이 쉽게 구현 가능
sum = 0
for i in range(1, 11):
    sum = sum + i

print(sum)
# 55
# range(1, 11)은 숫자1부터 10까지(1이상 11미만)의 숫자를 데이터로 갖는 객체이다
# 따라서 위 i변수에 리스트의 숫자가 1부터 10까지 하나씩 차례로 대입된다
#
# 60점 이상이면 합격이라는 문장을 출력하는 예제를 range 함수를 사용해서 작성해보자
marks = [90, 24, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다 합격입니다" % (number+1))
# len() 함수는 리스트 안의 요소의 개수를 돌려주는 함수이다 따라서 len(marks)는 5가 될것이고
# range(len(marks))는 range(5)가 되므로 number 변수에는 차례대로 0부터 4까지의 숫자가 대입된다
# marks[number]는 차례대로 90, 24, 67, 45, 80 값을 갖게 된다

# for와 range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')
# 2 4 5 6 10 12 14 16 18
# 3 6 9 12 15 18 21 24 27
# ...
# 9 18 27 36 45 54 63 72 81
#
# 매개변수 end를 넣어준 이유는?
# 해당 결과값을 출력할 때 다음줄로 넘기지 않고 그 줄에 계속해서 출력하기 위해서
# 그 다음에 이어지는 print(' ')는 단을 구분하기 위해 for문이 끝나면 결과값을 다음줄부터 출력하게 해준다

# 리스트 내포
# 리스트 내포의 문법
[표현식 for 항목 in 반복가능객체 if 조건문]

# 리스트 내포 사용하기
# 리스트 안에 for문을 포함하는 리스트내포(list comprehension)를 사용하면 좀 더 편리하고 직관적이다
normal = [1, 2, 3, 4]
result = []
for num in normal:
    result.append(num * 3)

print(result)
# [3, 6, 9, 12]
#
# 위 예제는comprehension 리스트의 각 항목에 3을 곱한 결과를 result 리스트에 담는 예제이다
# 이것을 리스트 내포를 사용하면 다음과 같이 간단하게 해결할 수 있다
comprehension = [1, 2, 3, 4]
result = [num * 3 for num in comprehension]
print(result)
# [3, 6, 9, 12]
#
# 만약 [1, 2, 3, 4] 중 짝수에만 3을 곱하고 싶다면 리스트 내포 안에 if조건을 사용할 수 있다
comprehension = [1, 2, 3, 4]
result = [num * 3 for num in a comprehension if num % 2 == 0]
print(result)
# [6, 12]

# for문이 2개 이상일 때 리스트 내포의 문법
[표현식 for 항목1 in 반복가능객체1 if 조건문1
        for 항목2 in 반복가능객체2 if 조건문2
        ...
        for 항목n in 반복가능객체n if 조건문n]

# 만약 리스트 내포를 사용하여 구구단의 모든 결과를 리스트에 담고 싶다면
result = [x*y for x in range(2, 10)
              for y in range(1, 10)]
print(result)
# 2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, ..., 9, 18, 27, 36, 45, 54, 63, 72, 81]

