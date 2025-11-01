# Nested Conditionals

print('Welcome to rollercoaster!')
height = int(input('Enter your height in cm: '))

if height >= 120:
    print('You can ride the ride!')
    age = int(input('Enter your age: '))
    if age <= 12:
        print('You have to pay $5')
    elif age <= 18:
        print('You have to pay $7')
    else:
        print('You have to pay $12')
else:
    print('You can not ride the ride!')
# in case of if, elif else case only one conditions will run or nested