"""pz 4 module"""
import os
import time
import re

def file_printing():
    """функция, которая выводит свой pid (os.getpid),
    pz4.txt, засыпает на 1 минуту (time.sleep),
    пишет в файл некоторую строку, засыпает на 3 минуты.
    В терминале выполните """
    print(os.getpid())
    time.sleep(60)
    file = open("pz4.txt", 'a')
    file.write("STRING --------------------------\n")
    time.sleep(60 * 3)
    file.close()
    # --------with
    time.sleep(60)
    with open("pz4.txt", 'a') as file:
        file.write("STRING ++++++++++++++++++++++++++\n")
    time.sleep(60 * 3)
    print('fin writing')

def path_checking():
    """программа, которая запрашивает у пользователя путь относительно
    его домашнего каталога и выполняет для него os.listdir """
    home_path = os.path.expanduser('~')
    print('home_path    ' + home_path)
    input_level = input('Enter the folder name:')
    while re.match(r'(\W)', input_level):
        input_level = input('Enter the folder name:')
    print('input_level  ' + input_level)
    next_level = os.path.normpath(os.path.join(home_path, input_level))
    print('next_level   ' + next_level)
    try:
        print('the dir contains: ' + os.listdir(next_level))
    except FileNotFoundError:
        print('Error! Bad dir name.')

def main():
    """main func"""
    file_printing()
    path_checking()

if __name__ == '__main__':
    main()
