import random

def main():
    """Угадайка!"""
    number = random.randint(0, 100)
    print('exit - сдаться')
    print('УГАДАЙКА')
    while True:
        answer = input('Угадайте число : ')

        if (answer == 'exit'):
            print('Загаданное число\n', number)
            print('ЗАВЕРШЕНИЕ - УГАДАЙКА')
            break
        if answer.isalpha() == True:
            continue

        answer = int(answer)

        if answer == number:
            print('Успех\n')
            break
        elif answer < number:
            print('Бери выше')
        else:
            print('Бери ниже')

if __name__=='__main__':
    main
