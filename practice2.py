# 1. 다음 코드의 결과값은 무엇일까?
"""
str = "Life is too short, You need python"

if "wife" in str: print("wife")
elif "python" in str and "You" not in str: print("python")
elif "shirt" not in str: print("shirt")
elif "need" in str: print("need")
else: print('none")
"""
-> shirt

# 2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구하라
sum = 0
num = 1
while num <= 1000:
    if num % 3 == 0:
        sum = sum + num
    num = num + 1

print(sum)
# 166833

# 3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성하라
"""
*
**
***
****
*****
"""
i = 0
while True:
    i = i + 1
    if i > 5:
        break
    print('*' * i)

# 4. for문을 사용해 1부터 100까지의 숫자를 출력해보자
for i in range(1, 101):
    print(i)

# 5. A 학급의 총 10명의 중간고사 점수는 아래와 같다 for문을 사용하여 평균 점수를 구하라
marks = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

sum = 0
for mark in marks:
    sum = sum + mark

avg = sum / len(marks)
print(avg)

# 6. 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드를 리스트 내포를 사용하여 표현하라
"""
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)
"""
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)
# [2, 6, 10]

