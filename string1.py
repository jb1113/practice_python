# 문자열
# 문자열을 만드는 방법

# 1. 큰따옴표(")로 양쪽 둘러싸기
"Hello World"

# 2. 작은따옴표(')로 양쪽 둘러싸기
'Python is fun'

# 3. 큰따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
"""Life is too short, You need python"""

# 4. 작은따옴표 3개를 연속(''')으로 써서 양쪽 둘러싸기
'''Life is too short, You need python'''


# 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을때
# 문자열에 작은따옴표(') 포함시키기
food = "Python's favorite food is perl"

# 문자열에 큰따옴표(") 포함시키기
say = '"Python is very easy." he says.'

# 백슬래시(\)를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함시키기
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."


# 여러 줄인 문자열을 변수에 대입하고 싶을 때
# 1. 줄 바꿈을 위한 이스케이프 코드 (\n) 삽입하기
multiline = "Life is too short\nYou need python"

# 2. 연속된 작은따옴표 3개 또는 큰따옴표 3개 사용하기
multiline = '''
Life is too short
You need python
'''

multiline = """
Life is too short
You need python
"""

