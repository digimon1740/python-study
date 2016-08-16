def hello():
    print("hello world!")


hello()


def my_abs(arg):
    if arg < 0:
        result = arg * -1
    else:
        result = arg
    return result


print(my_abs(-5))
print(my_abs(10))


# print(my_abs()) #error

def print_string(text, count):
    for i in range(count):
        print(text)


print_string('안녕하세요 이상훈 입니다', 3)


# 기본값 매개변수
def print_string(text, count=1):
    for i in range(count):
        print(text)


# 키워드 매개변수
def print_personnel(name, position='staff', nationality='Korea'):
    print('name = {0}'.format(name))
    print('position = {0}'.format(position))
    print('nationality = {0}'.format(nationality))


print_personnel(name='이상훈')
print_personnel(name='이상훈', nationality='ROK')
print_personnel(name='이상훈', position='회장')


# 가변 매개변수
def merge_string(*text_list):
    result = ''
    print(type(text_list))  # type은 tuple
    for s in text_list:
        result += s
    return result


print(merge_string('상훈이는 ', '프로그래밍 ', '공부하는중'))


def print_team(**players):
    for k in players.keys():
        print('{0} = {1}'.format(k, players[k]))


print_team(카시야스='GK', 호날두='FW', 알론소='MF', 페페='DF')


# 변수의 scope
def scope_test():
    a = 1
    print('a:{0}'.format(a))


a = 0
scope_test()

print('a:{0}'.format(a))


def scope_test():
    global a
    a = 1
    print('a:{0}'.format(a))


a = 0
scope_test()

print('a:{0}'.format(a))


# 재귀 함수
def some_func(count):
    if count > 0:
        some_func(count - 1)
    print(count)


some_func(10)


def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return factorial(n - 1) * n


print(factorial(100))


# 무한루프
# def no_idea():
#     print("나는 아무 생각이 없다.")
#     print("왜냐하면")
#     no_idea()
#
# no_idea()

# 함수를 변수에 담기
def print_something(a):
    print(a)


p = print_something
p(123)
p('abc')


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


flist = [plus, minus]
print(flist[0](1, 2))
print(flist[1](1, 2))

# 딕셔너리에 넣어 호출
flist = {'plus': plus, 'minus': minus}
print(flist['plus'](1, 2))
print(flist['minus'](1, 2))


# 함수의 매개변수로 사용
def hello_korean():
    print('안녕하세요')


def hello_english():
    print('Hello')


def greet(hello):
    hello()


greet(hello_korean)
greet(hello_english)


# 함수의 결과로써 반환
def get_greeting(where):
    if where == 'K':
        return hello_korean()
    else:
        return hello_english()


get_greeting('K')
get_greeting('E')

# 중첩함수 closure
import math


def stddev(*args):
    def mean():
        return sum(args) / len(args)

    def variance(m):
        total = 0
        for arg in args:
            total += (arg - m) ** 2
        return total / (len(args) - 1)

    v = variance(mean())
    return math.sqrt(v)


print(stddev(2.3, 1.7, 1.4, 0.7, 1.9))


def empty_function():
    pass


class empty_class():
    pass


# Class 는 pep8에서 CamelCase (CapWords)로 명명


class EmptyClass:
    pass


## 연습문제
def min(a, b):
    result = a

    if a > b:
        result = b

    return result


print(min(3, 4))
print(min(11, 1))


def print_personnel(name, position='staff', nationality='Korea'):
    print('name = {0}'.format(name))
    print('position = {0}'.format(position))
    print('nationality = {0}'.format(nationality))


print_personnel(name='이상훈')
print_personnel(name='이상훈', nationality='ROK')
print_personnel(name='이상훈', position='회장')
print_personnel('이상훈', position='회장')


# print_personnel(position='회장')


def average(*args):
    sum = 0

    for n in args:
        sum += n

    return sum / len(args)


def plus_or_minus(arg):
    if arg < 0:
        return "minus"
    elif arg > 0:
        return "plus"


print(plus_or_minus(0))


def print_starts(arg):
    for i in range(arg, 0, -1):

        for j in range(i):
            print('*', end='')

        print()

print_starts(10)