yes = ['да', 'yes', 'д', 'y', '+']
no = ['нет', 'no', 'н', 'n', '-']


def cycle():
    while True:
        print('Цикл работает!')
        while True:
            answer = input('Продолжать?').lower()
            if answer in no:
                print('Цикл остановлен')
                return
            if answer in yes:
                break
            print('Введено неверное значение. Повторите ввод!')


cycle()
