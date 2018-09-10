num_one = str(input('Введите слово: '))
num_two = str(input('Введите второе слово: '))


def compare_line(num_one, num_two):
    if not (isinstance(num_one, str) and isinstance(num_two, str)):
        print('0')
    elif num_one == num_two:
        print('1')
    elif len(num_one) >= len(num_two):
        print('2')
    elif num_one != num_two and num_two == 'learn':
        print('3')
    else:
        print('tz govno')


compare_line(num_one, num_two)

