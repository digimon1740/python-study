a = 0
if a:
    print("1")
else:
    print("2")

for i in range(1, 6):
    for j in range(i):
        print("*", end="", )  # end=""을 매개변수로 입력하면 줄바꿈을 출력하지 않음
    print()

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="", )
    print()

i = 0
while i < 5:
    j = i + 1
    while j > 0:
        print('*', end='')
        j -= 1
    print()
    i += 1

i = int(input())

if i < 0:
    print("0보다 작거나 같은 수는 입력할수 없습니다.")
else:
    while i > 0:
        j = i
        while j > 0:
            print('*', end='')
            j -= 1
        print()
        i -= 1
