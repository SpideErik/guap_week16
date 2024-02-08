from random import shuffle, sample


def make_ticket():
    return sample(list(range(1, 101)), 50)


def lottery():
    balls = list(range(1, 101))
    shuffle(balls)
    tickets = [make_ticket(), make_ticket()]

    for n, i in enumerate(balls[:75], 1):
        print(f'Ход номер - {n}. Выпало - {i}')
        for player in range(2):
            if i in tickets[player]:
                print(f'В билете игрока{player + 1} есть число {i}')
                tickets[player].remove(i)
                if not tickets[player]:
                    print(f'Игрок{player} выйграл!')
                    return
            else:
                print(f'В билете игрока{player} нет числа {i}')

    print('Список выпавших чисел:', balls[:75])
    for player in range(2):
        print(f'Игроку{player} не повезло с билетом!')
        print('Не выпавшие числа:', tickets[player])


lottery()
