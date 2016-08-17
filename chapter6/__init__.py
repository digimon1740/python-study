a = 0
if a: print("1")

else: print("2")

for i in range(1,6) :
    for j in range(i):

        print("*" , end = "",)

    print()

for i in range(5,0,-1) :
    for j in range(i):

        print("*" , end = "",)

    print()

i = 0
j = 0
while i <= 4:

    i = i+1
    j = 0

    while j < i:

        j = j + 1

        print("*" , end="",)

    print()

i = 6
j = 0
while i >= 1:

    i = i-1
    j = 0

    while j < i:

        j = j + 1

        print("*" , end="",)

    print()

while True:

    print("반복할 횟수를 입력하세요 : ")

    num = int(input())

    if num <= 0:

        print("0보다 작거나 같은수는 입력할 수 없습니다.")

    else:
        for i in range (1, num+1):
            for j in range(i):

                print("*", end="",)

            print()

        break



