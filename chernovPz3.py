import printer

def menu():
    print('\nВведите команду: \n1.покричи \n2.калькулятор \n3.угадайка \nq для выхода: \n')


def shout_on_me():
    print('ПОКРИЧИ')
    print('q - выход')
    while True:
        answer = input('Что ты сказал?  \r')
        if answer == 'q':
            print('Завершение - ПОКРИЧИ')
            break
        print('Сам ты ', answer.upper(), '. И не кричи на меня\n\n')

def calculator():
    print('КАЛЬКУЛЯТОР')
    print('q - выход')
    while True:
        answer = input('Введите выражение:  \n')
        if answer == 'q':
            print('Завершение - КАЛЬКУЛЯТОР')
            break
        try:
            num1, num2 = answer.split('+')
            print('Результат: ', int(num1) + int(num2), '.\n\n')
        except ValueError:
            print('Ошибочный ввод!  Пример: "56+212"')
            continue




def main():
    menu()
    COMMANDS = {
        '1' or 'покричи':shout_on_me,
        '2' or 'калькулятор': calculator,
        '3' or 'угадайка': printer.main,
        'q': exit
    }
    while True:
        answer = input()
        client_handler = COMMANDS.get(answer, menu)
        client_handler()
        menu()




if __name__ == '__main__':
    main()

