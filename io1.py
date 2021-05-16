# 사용자 입력과 출력
# 사용자 입력
# 사용자가 입력한 값을 변수에 대입하고 싶을 때는 어떻게 해야할까?

# input의 사용
str = input()
Life is too short, You need python
str
# 'Life is too short, You need python'

# 프롬프트를 띄워서 사용자 입력 받기
# 사용자에게 입력받을 때 문구 또는 질문이 나오도록 하고 싶은 경우
# input()의 괄호 안에 문구를 입력하여 프롬프트를 띄워주면된다
input("문구")
number = input("숫자를 입력하세요: ")
# 숫자를 입력하세요: 10
print(number)
# 10
number
# '10'

# print 자세히 알기
# 지금껏 print문이 수행해 온 이은 우리가 입력한 자료형을 출력하는 것이었다
# print의 사용예는 다음과 같다
a = 123
print(a)
# 123
a = 'Python'
print(a)
# Python
a = [1, 2, 3]
print(a)
# [1, 2, 3]
# 이제 print문으로 할 수 있는 일에 대해 조금 더 자세하게 알아보자

# 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
print("life" "is" "too short")
# lifeistoo short
print("life"+"is"+"too short")
# lifeistoo short
# 따옴표로 둘러싸인 문자열을 연속해서쓰면 + 연산을 한 것과 같다

# 문자열 띄어쓰기는 콤마(,)로 한다
print("life", "is", "too short")
# life is too short
# 콤마(,)를 사용하면 문자열 사이에 띄어쓰기를 할 수 있다

# 한줄에 결과값 출력하기
# 한줄에 결과값을 계속 이어서 출력하려면 매개변수 end를 사용해 끝 문자를 지정해야 한다
for i in range(10):
    print(i, end=' ')
# 0 1 2 3 4 5 6 7 8 9

