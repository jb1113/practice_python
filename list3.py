# 리스트의 수정과 삭제
# 리스트는 값을 수정하거나 삭제할 수 있다

# 리스트에서 값 수정하기
a = [1, 2, 3]
a[2] = 4
a
# [1, 2, 4]

# del 함수 사용해 리스트 요소 삭제하기
a = [1, 2, 3]
del a[1]
a
# [1, 3]

# del 함수는 파이썬이 자체적으로 가지고 있는 삭제 함수 이며 다음과 같이 사용
# del 객체
# 객체란 파이썬에서 사용되는 모든 자료형을 말한다

# 슬라이싱 기법을 사용하여 리스트의 요소 여러개를 한꺼번에 삭제
a = [1, 2, 3, 4, 5]
del a[2:]
a
# [1, 2]

# 리스트의 요소를 삭제하는 방법에는 2가지가 더 있다
# 리스트의 remove()와 pop() 함수를 사용하여 삭제하는 방법이 있다

