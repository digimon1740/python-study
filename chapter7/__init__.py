print ("1.")
def min(a,b):
    result = a

    if(a > b):
        result = b

    return result


print (min(3,4))
print (min(11,1))

print ("2.")
def print_personnel(name, position = 'staff', nationality = 'korea'):
    print ('name = {0}'.format(name))
    print ('position = {0}'.format(position))
    print ('nationality = {0}'.format(nationality))

print_personnel(name = 'kim')
print_personnel(name = 'kim', position='ceo')

print ("3.")
#

print ("4.")
def plus_or_minus(arg):
    if arg < 0:
        return 'minus'
    elif arg > 0:
        return 'plus'

result = plus_or_minus(0)
print (result)

print ("1.")
print ("1.")
print ("1.")
print ("1.")
print ("1.")
print ("1.")
print ("1.")
print ("1.")