from random import randint


score = 15
while score > 0:
    guess = randint(1, 5)
    answer = int(input('Какое число выбрал компьютер (1-5)?'))
    if guess == answer:
        print('Угадал загаданное число! Компьютер проиграл!')
        print(f'Счёт: {score}')
        break
    score -= guess
    print(f'Компьютер загадал {guess}')
    print(f'Счёт: {score}')
else:
    print('Кончились очки! Компьютер Победил!')
