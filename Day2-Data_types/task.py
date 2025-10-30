# subscripting
print('Hello'[4])
print('Hello'[-1])

# string
print('123'+'345')

# integer = whole number
print(123+345)

# large integers
print(123_456_789)

# float = floating point numbers(decimal numbers)
print(3.14159)

# boolean
print(True)
print(False)


# print(int('abc')) # this will give a value error

name_of_user='Anmol Pandey'

# print('the number of characters in the given name is' + len(input('enter the name\n'))) # will give error as len function return a int and we can't add string with int

# print('the number of characters in the given name is', len(input('enter the name\n'))) # we can do this or convert int to str
# print('the number of characters in the given name is ' + str(len(input('enter the name\n'))))

# Mathematical operators

print(234+21)
print(54-5)
print(23*4)
print(23/2)
print(23//2) # it returns only the integer part removes all te decimal, can be dangerous while working with scientific data (floor division)
print(2**5)

# PEMDAS( goes from left to right )

print(3*3+3/3-3)

# round function
num=27.5658
print(round(num,2))
print(round(num,3))

# f-string (formatted string)
print(f'the value of {num} is {num}')
'''
notes taken during the class
to print type of data in python: print(type(variable))

'''
