# Multiple if conditions

print('Welcome to rollercoaster!')
height = int(input('Enter your height in cm: '))
bill=0
if height >= 120:

    print('You can ride the ride!')
    age = int(input('Enter your age: '))
    if age <= 12:
        bill = 5
        print('You have to pay $5')
    elif age <= 18:
        bill = 7
        print('You have to pay $7')
    else:
        bill = 12
        print('You have to pay $12')

    want_photo = input('Do you want photo? (Y/N): ')
    if want_photo == 'y':
        bill=bill+3

    print(f'Your bill is: ${bill}')
else:
    print('You can not ride the ride!')