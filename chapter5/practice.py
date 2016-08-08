# 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9.10]

print(a[0:5])

# 리스트 결합
a = [1, 2, 3, 4]
b = [5, 6, 7]

print(a + b)

# 찹조 연산
a = [1, 2, 3, 4, 5]
a[2] = 30
print(a)

# 길이 알아내기
print(len(a))

# 리스트의 끝에 새 요소를 추가
a = [1, 2, 3]
a.append(4)
print(a)

# 기존 리스트에 다른 리스트를 이어 붙임
a = [1, 2, 3]
a.extend([4, 5, 6])
print(a)

# 해당 위치에 새 요소를 삽입
a = [2, 4, 5]
a.insert(0, 1)  # 0 위치(첫 번째)에 데이터 1을 삽입합니다.
print(a)
a.insert(2, 3)  # 2 위치(세 번째)에 데이터 3을 삽입합니다.
print(a)

# 입력한 데이터를 리스트에서 찾아 발견된 첫번째 요소를 제거
a = ['BMW', 'BENZ', 'VOLKWAGEN', 'AUDI']
a.remove('BMW')
print(a)

# 리스트의 마지막 요소를 제거
a = [1, 2, 3, 4, 5]
a.pop()
print(a)

# 특정 인덱스의 요소를 제거하고 싶을때
a = [1, 2, 3, 4, 5]
a.pop(2)
print(a)

# 입력한 데이터와 일치하는 첫 번째 요소의 인덱스를 반환
a = ['abc', 'def', 'ghi']
print(a.index('def'))

# 입력한 데이터와 일치하는 요소가 몇 개 있는지 셈
a = [1, 100, 2, 100, 3, 100]
print(a.count(100))
print(a.count(200))

# 리스트 내의 요소를 정렬 reverse = True 는 내림차순 아무것도 입력하지 않으면 오름차순
# reverse = True와 같이 이름을 명시하여 사용하는 매개변수를 "키워드 매개변수" 라고 함
a = [3, 4, 5, 1, 2]
a.sort()
print(a)

a.sort(reverse=True)
print(a)

# 리스트 내 요소의 순서를 뒤집는다
b = ['안', '녕', '하', '세', '요']
b.reverse()
print(b)

# 튜플
a = (1, 2, 3)
print(a)
print(type(a))

a = 1, 2, 3, 4
print(a)
print(type(a))

# 요소가 하나인 튜플 정의하기
a = (1)
print(a)
print(type(a))  # <class 'int'>

a = (1,)
print(a)
print(type(a))  # <class 'tuple'>

b = 1,
print(b)
print(type(b))  # <class 'tuple'>

# 튜플 슬라이싱
a = (1, 2, 3, 4, 5, 6)
print(a[:3])
print(a[4:6])

# + 연산자 결합
a = (1, 2, 3)
b = (4, 5, 6)

c = a + b
print(a)
print(b)
print(c)

# 튜플 패킹 : 여러 가지 데이터를 튜플로 묶는것
a = 1, 2, 3, '이상훈'
print(a)

# 튜플 언패킹 : 튜플의 각 요소를 여러 개의 변수에 할당하는 것
one, two, three, four = a
print(one)
print(two)
print(three)
print(four)

# 입력한 데이터와 일치하는 첫 번째 요소의 인덱스를 반환
a = ('abc', 'def', 'ghi')
print(a.index('def'))

# 입력한 데이터와 일치하는 요소가 몇 개 있는지 셈
a = (1,100,2,100,3,100)
print(a.count(100))
print(a.count(200))
