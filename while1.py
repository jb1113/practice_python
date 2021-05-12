# 반복문
# while문

# while문의 기본 구조
while 조건문:
    수행할 문장1
    수행할 문장2
    수행할 문장3
    ...

# 열 번 찍어 안 넘어가는 나무 없다
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %번 찍었습니다" % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다")
# 나무를  1번 찍었습니다
# 나무를  2번 찍었습니다
# 나무를  3번 찍었습니다
# 나무를  4번 찍었습니다
# 나무를  5번 찍었습니다
# 나무를  6번 찍었습니다
# 나무를  7번 찍었습니다
# 나무를  8번 찍었습니다
# 나무를  9번 찍었습니다
# 나무를 10번 찍었습니다
# 나무 넘어갑니다

# while문 만들기
prompt = """
    1. Add
    2. Del
    3. List
    4. Quit

    Enter number:
"""
number = 0
while number != 4:
    print(prompt)
    number = int(input())

# while문 강제로 빠져나가기
# break문을 사용한다
# 커피 자판기
coffee = 100
money = 3000
while money:
    print("돈을 받았으니 커피를 줍니다")
    coffee = coffee - 1
    print("남은 커피 양은 %d개 입니다" % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다 판매를 중지합니다")
        break

# 실제 커피 자판기 (coffee.py)
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다" % (money - 300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다")
        print("남은 커피의 양은 %d개 입니다" % coffee)

    if coffee == 0:
        print("커피가 다 떨어졌습니다 판매를 중지합니다")
        break

# while문의 맨 처음으로 돌아가기
# continue문을 사용한다
# 1부터 10까지의 숫자 중 홀수만 출력
num = 0
while num < 10:
    num = num + 1
    
    if num % 2 == 0:
        continue
    
    print(num)
# 1
# 3
# 5
# 7
# 9

# 무한루프
# 무한루프의 기본형태
while True:
    수행할 문장1
    수행할 문장2
    ...
# while문의 조건문이 True이므로 항상 참이 된다 따라서 while문 안에 있는 문장들은 무한하게 수행된다
while True:
    print("Ctrl + D를 눌러야 while문을 빠져나갈 수 있습니다")

