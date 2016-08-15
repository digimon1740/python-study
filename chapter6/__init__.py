print ("1.")
print (not False)
print (not 0)
print (not None)
print (not 'ABC')
print (not True)
print ("2.")
print (True and False)
print (True or not False)
print (False and not False)
print ("3.")
a = 0
if a:
    print('1')
else :
    print('2')
print ("4.")
for s in ['*', '**', '***', '****', '*****']:
    print(s)

print ("4.")
for s in range(0, 6, 1):
    for ss in range(s):
        print '*',
    print ("")

print ("5.")

for s in range(5, 0, -1):
    for ss in range(s):
        print '*',
    print ("")

print ("6.")

answer = int(input())

if answer < 0 :
    print('aaa')

for s in range(0, answer):
    for ss in range(s):
        print '*',
    print ("")
