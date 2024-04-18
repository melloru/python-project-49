from math import gcd
import prompt
import random
from brain_games.scripts import brain_game


def main():
    name = brain_game.main()
    print('Find the greatest common divisor of given numbers.')
    for i in range(0, 3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 30)
        print(f'Question: {num1} {num2}')
        answer = prompt.string('Your answer: ')

        correct_answer = gcd(num1, num2)

        if brain_game.logic(answer, correct_answer, name) is not None:
            return

    print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
