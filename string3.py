# 문자열 인덱싱과 슬라이싱

# 문자열 인덱싱
str = "Life is too short, You need Python"
#      0         1         2         3
#      0123456789012345678901234567890123
# str[3] = 'e'
# str[0] = 'L'
# str[-1] = 'n'
# str[-0] = 'L'
# str[-2] = 'o'

# 문자열 슬라이싱
str = "Life is too short, You need Python"
#      0         1         2         3
#      0123456789012345678901234567890123
# word = str[0] + str[1] + str[2] + str[3]
# word = 'Life'
# word = str[0:4] = 'Life'
# word = str[0:3] = 'Lif'
# 슬라이싱 기법으로 str[시작번호 : 끝번호]를 지정할 때 끝 번호에 해당하는 것은 포함하지 않는다
# str[0:3]
# 0 <= str < 3
# str[0], str[1], str[2] 만 해당한다
# str[5:7] = 'is'
# str[12:17] = 'short'

# str[시작번호 : 끝번호]에서 끝번호를 생략하면 시작번호부터 그 문자열의 끝까지 뽑아낸다
# str[19:] = 'You need Python'
# str[시작번호 : 끝번호]에서 시작번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아낸다
# str[:17] = 'Life is too short'
# str[시작번호 : 끝번호]에서 시작번호와 끝번호를 둘 다 생략하면 문자열의 처음부터 끝까지 뽑아낸다
# str[:] = 'Life is too short, You need Python'

# str[19:-7] = 'You need' (str[-8]까지를 말하므로 이 역시 str[-7]은 포함하지 않는다)

str = "20200331Rainy"
#      0         1
#      0123456789012
date = str[:8]
weather = str[8:]
# date = '20200331'
# weather = 'Rainy'
year = str[:4]
day = str[4:8]
# year = '2020'
# day = '0331'


# "Pithon"이라는 문자열을 "Python"으로 바꾸려면?
str = "Pithon"
str[1] = 'y'
# 오류 발생
# 문자열의 요소값은 바꿀 수 있는 값이 아니기 때문이다 (immutable)
# str[:1] = 'P'
# str[2:] = 'thon'
# str[:1] + 'y' + str[2:] = 'Python'
