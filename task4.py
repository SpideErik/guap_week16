from random import shuffle, sample


def make_random_list(n):
    return sample(list(range(1, 101)), n)


def lottery():
    balls = make_random_list(75)
    tickets = [make_random_list(50), make_random_list(50)]

    for n, i in enumerate(balls, 1):
        print(f'Ход номер - {n}. Выпало - {i}')
        for player in range(2):
            if i in tickets[player]:
                print(f'В билете игрока{player+1} есть число {i}')
                tickets[player].remove(i)
                if not tickets[player]:
                    print(f'Игрок{player+1} выйграл!')
                    return
            else:
                print(f'В билете игрока{player+1} нет числа {i}')

    print('Список выпавших чисел:', balls)
    for player in range(2):
        print(f'Игроку{player+1} не повезло с билетом!')
        print('Не выпавшие числа:', tickets[player])


lottery()
