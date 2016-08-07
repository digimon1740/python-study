print(123 + 456)

print('123' + '456')

# 다음 코드 중 잘못된 것을 고르세요.
print(123 + 456)
print(1.23 / 4.56)
# print('123' * '456')

a = 10
a -= 5
print(a)

a = 'Good Morning'
print(a[:4])

print(len('안녕하세요'))

print(4 >> 2)

print(4 << 2)

print(4 | 3)

print(4 & 3)

x = 0b1001
print(x)

x = 0xFF
print(x)

x = 0xF0 | 0x0F
print(x)

a = '{0} {1}'.format('Mario', 40)
b = '{name} {age}'.format(name='Luigi', age=35)

print(a)
print(b)


##문자열 메소드##

#원본 문자열이 매개변수로 입력한 문자열로 시작되는지를 판단합니다.
a = 'Hello'
print(a.startswith('He'))
print(a.startswith('lo'))

#원본 문자열이 매개변수로 입력한 문자열로 끝나는지를 판단합니다.
#결과는 True 또는 False로 나옵니다.
print(a.endswith('He'))
print(a.endswith('lo'))

#원본 문자열 안에 매개변수로 입력한 문자열이 존재하는 위치를 앞에서부터 찾습니다.
#존재하지 않으면 -1을 결과로 내놓습니다.
print(a.find('li'))
print(a.find('H'))
print(a.find('K'))

#원본 문자열 안에 매개변수로 입력한 문자열이 존재하는 위치를 뒤에서부터 찾습니다.
#존재하지 않으면 -1을 결과로 내놓습니다
print(a.rfind('H'))
print(a.rfind('lo'))
print(a.rfind('M'))

#원본 문자열 안에 매개변수로 입력한 문자열이 몇 번 등장하는지를 셉니다.
print(a.count('l'))

#원본 문자열 왼쪽에 있는 공백을 제거합니다.
print('    Left Strip'.lstrip())

#원본 문자열 오른쪽에 있는 공백을 제거합니다.
print('Right Strip    '.rstrip())

#원본 문자열 양쪽에 있는 공백을 제거합니다.
print('    Strip    '.strip())

# 원본 문자열이 숫자와 기호를 제외한 알파벳영문 한글 등)으로만 이루어져 있는지를 평가합니다.
print('ABCDefgh'.isalpha())

# 원본 문자열이 수로만 이루어져 있는지를 평가합니다
print('1234'.isnumeric())

# 원본 문자열이 알파벳과 수로만 이루어져 있는지를 평가합니다
print('1234ABC'.isalnum())
print('1234'.isalnum())
print('ABC'.isalnum())
print('1234 ABC'.isalnum())

#원본 문자열에서 찾고자 하는 문자열을 바꾸고자 하는 문자열로 변경합니다
a = 'Hello, World'
b = a.replace('World','Korea')
print(a)
print(b)

#매개변수로 입력한 문자열을 기준으로 원본 문자열을 나눠 리스트를 만듭니다
#리스트는 목록을 다루는 자료형이며 5장에서 자세히 다룹니다
a = 'Apple, Orange, Kiwi'
b = a.split(',')
print(b)
print(type(b))

#원본 문자열을 모두 대문자로 바꾼 문자열을 내놓습니다
a = 'lower case'
b = a.upper()
print(a)
print(b)

#원본 문자열을 모두 소문자로 바꾼 문자열을 내놓습니다
a = 'UPPER CASE'
b = a.lower()
print(a)
print(b)

#형식을 갖춘 문자열을 만들 때 사용합니다. 문자열 안에 중괄호 '{'와 '}'로 다른 데이터가 들어갈 자리를
#만들어 두고 format() 함수를 호출할 떄 이 자리에 들어갈 데이터를 순서대로 넣어주면 원하는 형식의
#문자열을 만들어 낼 수 있습니다
a = 'My name is {0}. Iam {1} years old.'.format('Mario', 40)
print(a)

b = 'My name is {name}. I am {age} years old.'.format(name='Luigi', age=35)
print(b)
