import printer

def group_parser(group):
    if group == 'Q':
        return
    if group == 'ПОКРИЧИ':
        print('%s - ВЫБРАНО ' % group)
        shout_on_me()
    elif group == 'КАЛЬКУЛЯТОР':
        print('%s - ВЫБРАНО ' % group)
        calculator()
    elif group == 'УГАДАЙКА':
        print('%s - ВЫБРАНО ' % group)
        printer.main()
    else:
        print('%s - Непонятная команда ' % group)

def shout_on_me():
    answer = ''
    print('q - выход')
    while answer != 'exit' and answer != 'q':
        answer = input('Что ты сказал?  \r')
        print('Сам ты ', answer.upper() ,'. И не кричи на меня\n\n')

def calculator():
    answer = ''
    print('q - выход')
    while answer != 'exit' and answer != 'q':
        try:
            answer = input('Введите выражение:  \r')
            num1, num2 = answer.split('+')
            print('Результат: ', int(num1)+int(num2) ,'.\n\n')
        except ValueError:
            print('Ошибочный ввод! Пример: "56+212"')
            continue

def main():
    """Определятор (покричи калькулятор угадайка)"""
    #group_parser('abc')
    #for group_num in range (7331, 7336):
        #group = str(group_num)
        #group_parser(group)

    answer = ''
    while answer != 'exit' and answer != 'q':
        answer = input('Введите команду (угадайка/покричи/калькулятор/q для выхода): \r')
        group_parser(answer.upper())
        continue
    print('До свидания!')

if __name__=='__main__':
    main()
    
