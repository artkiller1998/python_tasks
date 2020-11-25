#!/usr/bin/python3
# это файл pz4.py
import random

class Guesser():
    """Play a 'guess a number' game"""
    def __init__(self):
        """Init a random number for guesser"""
        self.rnd = random.randint(0, 100)

    def check(self, guess):
        """Check if guess was right
        Args:
            guess: str from user that guess a number

        Returns:
            0 if correct
            1 if guess > self.rnd
            -1 if guess < self.rnd

        Raises:
            ValueError: if guess cant be converted to int.
        """
        if guess == self.rnd:
            return 0
        elif guess > self.rnd:
            return 1
        else:
            return -1

    def play(self):
        """Start a guess game"""
        while True:
            answer = input('Угадайте число: ')
            # если ввести не число, то всё поломается. Обработку ошибок рассмотрим позже
            answer = int(answer)

            # как работает эта конструкция?
            check = self.check(answer)
            if not check:
                print('\nУспех! Верно угадано число {0}'.format(self.rnd))
                break
            elif check == 1:
                print('Бери ниже')
            elif check == -1:
                print('Бери выше')
            else:
                print('Что-то сломалось')

if __name__ == '__main__':
    guesser = Guesser()
    guesser.play()