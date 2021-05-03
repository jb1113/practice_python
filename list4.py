# 리스트 관련 함수들

# 리스트에 요소 추가 (append)
a = [1, 2, 3]
a.append(4)
a
# [1, 2, 3, 4]
a.append([5, 6])
a
# [1, 2, 3, 4, [5, 6]]

# 리스트 정렬 (sort)
a = [1, 4, 3, 2]
a.sort()
a
# [1, 2, 3, 4]

b = ['a', 'c', 'b']
b.sort()
b
# ['a', 'b', 'c']

# 리스트 뒤집기 (reverse)
# reverse 함수는 리스트를 역순으로 뒤집어 준다
# 이때 리스트 요소들을 순서대로 정렬한 다음 다시 역순으로 정렬하는 것이 아니라 그저 현재의 리스트를 그대로 거꾸로 뒤집는다
a = ['a', 'c', 'b']
a.reverse()
a
# ['b', 'c', 'a']

# 위치 반환 (index)
a = [1, 2, 3]
a.index(3)
# 2
a.index(1)
# 0
a.index(0)
# 값 0은 리스트 a에 존재하지 않으므로 값 오류(ValueError) 발생
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# ValueError: 0 is not in list

# 리스트 요소 삽입 (insert)
# insert(a, b)는 a번째 위치에 b를 삽입하는 함수이다
a = [1, 2, 3]
a.insert(0, 4)
a
# [4, 1, 2, 3]
a.insert(3, 5)
a
# [4, 1, 2, 5, 3]

# 리스트 요소 제거 (remove)
# remove(x)는 리스트에서 첫번째로 나오는 x를 삭제하는 함수이다
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a
# [1, 2, 1, 2, 3]
a.remove(3)
a
# [1, 2, 1, 2]

# 리스트 요소 끄집어내기 (pop)
# pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제하는 함수이다
a = [1, 2, 3]
a.pop()
# 3
a
# [1, 2]
# pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소는 삭제한다
a = [1, 2, 3]
a.pop(1)
# 2
a
# [1, 3]

# 리스트에 포함된 요소 x의 개수 세기 (count)
# count(x)는 리스트 안에 x가 몇 개 있는지 조사하여 그 개수를 돌려주는 함수이다
a = [1, 2, 3, 1]
a.count(1)
# 2

# 리스트 확장(extend)
# extend(x)에서 x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더하게 된다
a = [1, 2, 3]
a.extend([4, 5])
a
# [1, 2, 3, 4, 5]
b = [6, 7]
a.extend(b)
a
# [1, 2, 3, 4, 5, 6, 7]
# a.extend([4, 5])는 a += [4, 5]와 동일하다

