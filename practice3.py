# 1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수를 작성해보자
def is_odd(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
# lambda와 조건부 표현식(conditional expression) 사용
is_odd = lambda number : "even" if number % 2 == 0 else "odd"
# 조건부 표현식
조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
# lambda
lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식

# 2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성하라 (입력의 개수는 정해지지 않음)
def avg_number(*args):
    sum = 0
    for i in args:
        sum = sum + i
    avg = sum / len(args)
    return avg

# 3. 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다
"""
input1 = input("첫번째 숫자를 입력하세요: ")
input2 = input("두번째 숫자를 입력하세요: ")

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
"""
# 이 프로그램을 수행하면 다음과 같다
"""
첫번째 숫자를 입력하세요: 3
두번째 숫자를 입력하세요: 6
두 수의 합은 36입니다
"""
# 3과 6을 입력했을때 9가 아닌 36이라는 결과값을 돌려주었다 이 프로그램의 오류를 수정해보자
# (int 함수를 사용해보자)
input1 = int(input("첫번째 숫자를 입력하세요: "))
input2 = int(input("두번째 숫자를 입력하세요: "))

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
# 입력은 항상 문자열이므로 숫자로 변경해 주어야한다
# total = int(input1) + int(input2) 도 가능

# 4. 다음 중 출력 결과가 다른 하나를 골라라
"""
1. print("you" "need" "python")
2. print("you"+"need"+"python")
3. print("you", "need", "python")
4. print("".join(["you", "need", "python"]))
"""
# 3을 제외하고 'youneedpython'으로 결과값이 동일하다
# 콤마(,)가 있는 경우 공백이 삽입되어 더해진다 'you need python'

# 5. 아래는 "test.txt"라는 파일에 "Life is too short"문자열을 저장한 후 다시 그 파일을 읽어 출력하는 프로그램이다
"""
file1 = open("test.txt", 'w')
file1.write("Life is too short")

file2 = open("test.txt", 'r')
print(file2.read())
"""
# 이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다
# 우리가 예쌍한 값을 출력할 수 있도록 프로그램을 수정해보자
file1 = open("test.txt", 'w')
file1.write("Life is too short")
file1.close()   # 열린 파일객체를 닫는다

file2 = open("test.txt", 'r')
print(file2.read())
file2.close()
# 문제의 예와 같이 파일을 닫지 않은 상태에서 다시 열면 파일에 저장한 데이터를 읽을 수 없다
# 따라서 열린 파일 객체를 close()로 닫아준 후 다시 열어서 파일의 내용을 읽어야 한다
# 또는 close를 명시적으로 사용할 필요가 없는 with 구문을 사용하면 다음과 같다
with open("test.txt", 'w') as file1:
    file1.write("Life is too short")
with open("test.txt", 'r') as file2:
    print(file2.read())

# 6. 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해보자
# 단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다)
"""
data = input("저장할 내용을 입력하세요: ")
file = open("test.txt", 'a')
file.write(data)
file.write('\n')
file.close()
"""
file = open("test.txt", 'a')
while True:
    data = input()
    if not data:
        break
    file.write(data + '\n')

# 7. 다음과 같은 내용을 지닌 파일 "test.txt"가 있다
# 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장하도록 하라
# (replace 함수를 사용해보자)
"""
Life is too short
You need java
"""
file1 = open("test.txt", 'r')
read_data = file1.read()
read_data = read_data.replace('java', 'python')
file1.close()

file2 = open("test.txt", 'w')
file2.write(read_data)
file2.close()
# 파일을 모두 읽은 후에 문자열의 replace 함수를 사용하여 java라는 문자열을 python으로 변경한 다음 저장한다
str = ""
read_file = open("test.txt", 'r')
lines = read_file.readlines()
for line in lines:
    if "java" in line:
        str = str + line.replace("java", "python")
#        temp_str = ''.join(line)
#        str = str + temp_str.replace("java", "python")
    else:
        str = str + line
read_file.close()

write_file = open("test.txt", 'w')
write_file.write(str)
write_file.close()

