def get_summ():
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        sum_num = num_one + num_two
        print(int(sum_num))
    except ValueError:
        print('Некоректный ввод!')


get_summ()
