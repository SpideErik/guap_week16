from random import sample


names = ['Eric', 'Roma', 'Vita', 'Anna', 'Dima', 'Vlad', 'Elena', 'Ivan', 'Oleg', 'Liza']

cnt = int(input('Сколько имён может загадать компьютер?'))

guess = sample(names, cnt)
errors = 0
while errors < 5:
    print(f'    Варианты:\n    {names}')
    name = input('Какой вариант выберешь?').title()
    if name in guess:
        print(f'Угадал! {name} одно из загаданных компьютером имён')
        names.remove(name)
        guess.remove(name)
        if not guess:
            print('Победа! Ты угадал все имена!')
            break
    else:
        print(f'Неверно! Имя: {name} компьютер не загадывал')
        errors += 1
else:
    print('Поражение! Кончились попытки!')
