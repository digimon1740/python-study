def min(a, b):
    result = a

    if (a > b):
        result = b

    return result


def my_abs(arg):
    if (arg < 0):
        result = agr * -1

    else:
        result = agr8u

    return result


def hello():
    print("hello world!")

hello()


def my_abs(arg):  # 매개변수
    if (agr < 0):
        result = arg * -1
    else:
        result = arg

    return result


def print_string(text, count):
    for i in range(count):
        print(text)

    print_string('안녕하세요', 3)


def print_string(text, count=1):  # 매개변수를 정의할 때 값을 할당해 놓으면 기본값 매개변수가 됩니다.
    for i in range(count):
        print(text)


print_string("안녕하세요")  # 호출할 때 두 번째 매개변수를 생략하면 기본값 1이 사용됩니다.
print_string("안녕하세요", 2)


def print_personnel(name, position='staff', nationality='Korea'):
    print('name = {0}'.format(name))
    print('position = {0}'.format(position))
    print('nationality = {0}'.format(nationality))


print_personnel(name='엄태호')  # positron과 antionality는 기본값이 사용됩니다.
name = 엄태호
position = staff
nationality = Korea

print_personnel(name='엄태호', nationality="ROK")  # position만이 기본값을 사용합니다.
name = 엄태호
position = staff
nationality = ROK

print_personnel(name='엄태호', position='인턴')  # nationality 만이 기본값을 사용합니다.
name = 엄태호
position = 인턴
nationality = Korea


def merge_string(*text_list):
    result = ''
    for s in text_list:
        result = result + s

    return result


merge_string('아버지가', '방에', '들어가신다.')
'아버지가방에들어가신다.'


def print_team(**players):  # 매개변수 앞에 **를 붙이면 딕셔너리 가변 매개변수가 됩니다.
    for k in players.keys():
        print('{0} = {1}'.format(k, players[k]))


print_team(카시야스="GK", 호날두='FW', 알론소='MF', 페페='DF')
카시야스 = GK
페페 = 'DF'
알론소 = 'MF'
호날두 = 'FW'


def print_args(argc, *argv):
    for i in range(argc):
        print(argv[i])


print_args(3, "argv1", "argv2", "argv3")
argv1
argv2
argv3

print_args(argc=3, "argv1", "argv2", "argv3")  # 가변 매개변수 앞에 정의된 일반 매개변수는
# 키워드 매개변수로 호출할 수 없습니다.8
syntaxError: non - keyword
arg
after
ketword
arg


def print_args(*argv, argc):
    for i in range(argc):
        print(argv[i])


print_args("argv1", "argv2", "argv3", argc=3)  # 가변 매개변수 뒤에 정의된 일반 매개변수는 반드시 키워드
# 매개변수로 호출해야 한다.
argv1
argv2
argv3

print_args("argv1", "argv2", "argv3", 3)
Traceback(most
recent
call
last):
File
"<pyshell#15>", line
1, in < module >
print_args("argv1", "argv2", "argv3", 3)
TypeError: print_args()
missing
1
required
Keyword - only
argument: 'agrc'


def multiply(a, b):
    return a * b  # return문은 함수의 실행을 존료시키고 자신에게 넘겨진 데이터를 호출자에게 전달합니다.


result = multiply(2, 3)
result
6
