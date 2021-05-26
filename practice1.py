# 1. 과목별 점수는 다음과 같다 평균 점수를 구하라
kor = 80
eng = 75
math = 55
sum = kor + eng + math
avg = sum / 3
print(avg)

# 2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법은 무엇인가
number = 13
print(number % 2)

# 3. 주민등록번호를 연월일 부분과 그 뒤의 숫자부분으로 나누어 출력하라
pin = "891113-1234567"
birth = pin[:6]
num = pin[7:]
print(birth)
print(num)

# 4. 주민등록번호에서 성별을 나타내는 숫자를 출력해보자
print(pin[7])

# 5. 다음 문자열 a:b:c:d를 replace 함수를 사용하여 a#b#c#d로 바꾸어라
str = "a:b:c:d"
after = str.replace(":", "#")
print(after)

# 6. [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어라
listA = [1, 3, 5, 4, 2]
print(listA)
listA.sort()
print(listA)
listA.reverse()
print(listA)

# 7. ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력하라
listA = ['Life', 'is', 'too', 'short']
str = listA[0] + " " + listA[1] + " " + listA[2] + " " + listA[3]
result = " ".join(listA)
print(result)
print(str)

# 8. (1, 2, 3) 튜플에 값 4를 추가하여 (1, 2, 3, 4)를 출력하라
tupleA = (1, 2, 3)
tupleA = tupleA + (4, )
print(tupleA)
# tuple에 (4, )라는 튜플을 더하면 된다
# 단 이때 만들어지는 tuple + (4, )의 결과는 tuple의 값이 변경되는 것이 아니라(튜플은 값을 변경할 수 없다) 새로운 튜플이 생성되고 그 값이 tuple 변수에 대입되는 것이다
# 다음을 실행해보면 tuple의 고유값이 변경됨을 확인할 수 있다
tupleA = (1, 2, 3)
print(id(tupleA))
tupleA = tupleA + (4, )
print(tupleA)
print(id(tupleA))

# 9. 오류가 발생하는 경우를 고르고 그 이유를 설명하라
# 딕셔너리의 Key 값은 immutable 해야 하지만 list는 값이 변할 수 있으므로 Key값으로 사용할 수 없다

# 10. 딕셔너리에서 'B'에 해당되는 값을 추출해보자
dictionaryA = {'A' : 90, 'B' : 80, 'C' : 70}
popItem = dictionaryA.pop('B')
print(popItem)
print(dictionaryA)

# 11. 리스트에서 중복 숫자를 제거하라
listA = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
setA = set(listA)
print(setA)
listB = list(setA)
print(listB)

# 12. 동일한 값에 여러 개의 변수를 선언할 수 있는데 다음과 같이 선언한 후 a의 두번째 요소값을 변경하면 b값은 어떻게 되는가?
listA = listB = [1, 2, 3]
listA[1] = 4
print(listB)
